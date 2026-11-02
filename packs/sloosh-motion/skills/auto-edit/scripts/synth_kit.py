#!/usr/bin/env python3
"""Make the sound kit and an optional music bed on this computer, with no network and no service.

usage: python synth_kit.py --project <dir> [--music --drop-at 8.0 --bpm 120 [--length 14]] [--seed 7] [--force]

Writes 48 kHz stereo 16-bit files:
  <dir>/audio/sfx/<name>.wav   whoosh_air whoosh_sub boom punch odometer riser shimmer
                               lights_off key_tap glitch swipe portal
  <dir>/audio/music.wav        with --music: an instrumental bed, quiet until a drop at --drop-at
                               seconds, then a kick on every beat at --bpm
These are plain synthesized sounds. Use them when the user has no licensed sounds and no Sloosh
Space fits, or as placeholders. Run audio_prep.py afterwards: it measures every sound and finds
the drop. An existing file is kept unless --force is given. Each file written is printed.
"""
import argparse, os, sys
try:
    import numpy as np
    import scipy.io.wavfile as wf
    from scipy.signal import stft, istft, fftconvolve
except ImportError:
    sys.exit('Missing Python packages: numpy and scipy. Ask the user before you install anything, then rerun.')

SR = 48000
RNG = np.random.default_rng(7)


def t_axis(sec):
    return np.arange(int(round(sec * SR))) / SR


def noise(sec):
    return RNG.standard_normal(int(round(sec * SR))).astype(np.float64)


def env_ad(t, peak, attack_pow=2.0, decay_pow=2.0):
    """Rise to 1 at `peak` seconds, then fall to 0 at the end."""
    end = t[-1] if len(t) else 1.0
    up = np.clip(t / max(peak, 1e-4), 0, 1) ** attack_pow
    down = np.clip((end - t) / max(end - peak, 1e-4), 0, 1) ** decay_pow
    return np.where(t <= peak, up, down)


def exp_decay(t, tau):
    return np.exp(-t / tau)


def band_path(x, centres, width=0.6):
    """Filter `x` through a band whose centre follows the Hz values in `centres`, spread evenly
    over the sound. `width` is the band width in octaves."""
    n = len(x)
    xp = np.pad(x, (0, max(0, 4096 - n)))         # the transform needs a few windows of signal
    f, tt, Z = stft(xp, SR, nperseg=1024, noverlap=768)
    k = np.clip(tt / max(n / SR, 1e-6), 0, 1)
    centre = np.exp(np.interp(k, np.linspace(0, 1, len(centres)), np.log(centres)))
    oct_ = np.log2(np.maximum(f[:, None], 1.0) / centre[None, :])
    Z = Z * np.exp(-0.5 * (oct_ / width) ** 2)
    _, y = istft(Z, SR, nperseg=1024, noverlap=768)
    return y[:n] if len(y) >= n else np.pad(y, (0, n - len(y)))


def band_sweep(x, f_start, f_end, width=0.6):
    """Band filter whose centre glides from f_start to f_end Hz."""
    return band_path(x, [f_start, f_end], width)


def chirp(t, f0, f1, curve=1.0):
    """Sine whose pitch glides from f0 to f1 (exponential glide, `curve` > 1 drops early)."""
    k = (t / max(t[-1], 1e-6)) ** (1.0 / curve)
    freq = f0 * (f1 / f0) ** k
    return np.sin(2 * np.pi * np.cumsum(freq) / SR)


def room(x, sec=0.6, mix=0.18):
    ir = noise(sec) * exp_decay(t_axis(sec), sec / 5)
    ir /= np.sqrt((ir ** 2).sum()) + 1e-9
    wet = fftconvolve(x, ir)[:len(x)]
    return x * (1 - mix) + wet * mix


def soft(x, drive=1.5):
    return np.tanh(x * drive) / np.tanh(drive)


def stereo(x, pan=None, width=0.0):
    """Mono to stereo. `pan` is a scalar or an array from -1 (left) to 1 (right)."""
    p = np.zeros_like(x) if pan is None else np.broadcast_to(pan, x.shape)
    left = x * np.cos((p + 1) * np.pi / 4) * np.sqrt(2)
    right = x * np.sin((p + 1) * np.pi / 4) * np.sqrt(2)
    if width:
        d = int(0.011 * SR)
        right = (1 - width) * right + width * np.concatenate([np.zeros(d), right[:-d]])
    return np.stack([left, right], 1)


# ---------------------------------------------------------------- the kit
def whoosh_air():
    t = t_axis(1.2)
    x = band_path(noise(1.2), [400, 1400, 3000, 900], width=0.7) * env_ad(t, 0.7, 2.2, 1.6)
    return stereo(room(x, 0.5, 0.15), pan=np.linspace(-0.7, 0.7, len(t)), width=0.3)


def whoosh_sub():
    t = t_axis(1.0)
    tone = chirp(t, 90, 38, 0.8)
    rumble = band_sweep(noise(1.0), 120, 60, width=0.8)
    x = (0.8 * tone + 0.5 * rumble / (np.abs(rumble).max() + 1e-9)) * env_ad(t, 0.6, 2.0, 1.4)
    return stereo(x)


def boom():
    t = t_axis(2.5)
    body = chirp(t, 82, 34, 3.0) * exp_decay(t, 0.55)
    hit = band_sweep(noise(2.5), 900, 200, width=1.2) * exp_decay(t, 0.05)
    tail = band_sweep(noise(2.5), 300, 120, width=1.0) * exp_decay(t, 0.7) * 0.25
    x = soft(1.1 * body + 0.6 * hit / (np.abs(hit).max() + 1e-9) + tail, 1.8)
    return stereo(room(x, 1.2, 0.22), width=0.25)


def punch():
    t = t_axis(0.5)
    body = chirp(t, 140, 48, 3.0) * exp_decay(t, 0.09)
    click = band_sweep(noise(0.5), 3000, 1500, width=1.0) * exp_decay(t, 0.006)
    x = soft(body + 0.5 * click / (np.abs(click).max() + 1e-9), 2.0)
    return stereo(x)


def _tick(sec=0.03, f=2400):
    t = t_axis(sec)
    return (np.sin(2 * np.pi * f * t) * 0.6 + band_sweep(noise(sec), f * 1.5, f * 1.5, 0.5)) * exp_decay(t, 0.004)


def odometer():
    sec = 1.2
    out = np.zeros(int(sec * SR))
    k = np.linspace(0, 1, 26)
    times = 1.0 * (1 - (1 - k) ** 2.2)             # fast ticks first, slowing into the landing
    tk = _tick()
    for i, tt in enumerate(times):
        a = int(tt * SR); g = 0.55 + 0.45 * (i / len(times))
        out[a:a + len(tk)] += g * tk[:len(out) - a]
    return stereo(room(out, 0.3, 0.12), width=0.2)


def riser():
    t = t_axis(3.0)
    air = band_sweep(noise(3.0), 300, 6500, width=0.8)
    air /= np.abs(air).max() + 1e-9
    saw = sum(np.sin(2 * np.pi * np.cumsum(220 * h * 2 ** (2 * t / 3.0)) / SR) / h for h in range(1, 7))
    e = (t / 3.0) ** 2.4
    x = (0.7 * air + 0.25 * saw / 2.5) * e
    x[-int(0.004 * SR):] *= np.linspace(1, 0, int(0.004 * SR))
    return stereo(x, width=0.35)


def shimmer():
    t = t_axis(2.0)
    x = np.zeros_like(t)
    for f in (2093, 2637, 3136, 4186, 5274):
        x += np.sin(2 * np.pi * f * t + RNG.uniform(0, 6.28)) * (0.6 + 0.4 * np.sin(2 * np.pi * RNG.uniform(5, 9) * t))
    x *= env_ad(t, 0.35, 1.5, 2.0) / 5
    return stereo(room(x, 1.5, 0.35), pan=0.3 * np.sin(2 * np.pi * 0.7 * t), width=0.4)


def lights_off():
    t = t_axis(0.8)
    clack = band_sweep(noise(0.8), 2500, 1800, width=0.7) * exp_decay(t, 0.008)
    thunk = chirp(t, 110, 60, 2.0) * exp_decay(t, 0.08)
    hum = np.sin(2 * np.pi * 100 * t) * 0.15 * exp_decay(t, 0.25)
    x = 0.7 * clack / (np.abs(clack).max() + 1e-9) + 0.8 * thunk + hum
    return stereo(room(x, 0.7, 0.25))


def key_tap():
    t = t_axis(0.08)
    x = band_sweep(noise(0.08), 4200, 3000, width=0.9) * exp_decay(t, 0.007)
    x += 0.3 * np.sin(2 * np.pi * 900 * t) * exp_decay(t, 0.01)
    return stereo(x)


def glitch():
    sec = 0.6
    out = np.zeros(int(sec * SR))
    pos = 0
    while pos < len(out):
        n = int(RNG.uniform(0.015, 0.06) * SR)
        tt = np.arange(n) / SR
        if RNG.random() < 0.5:
            seg = np.sign(np.sin(2 * np.pi * RNG.uniform(200, 1800) * tt))
        else:
            seg = band_sweep(noise(n / SR), RNG.uniform(500, 5000), RNG.uniform(500, 5000), 0.6)
            seg /= np.abs(seg).max() + 1e-9
        seg = np.round(seg * 6) / 6                 # crushed to a few levels
        out[pos:pos + n] = seg[:len(out) - pos] * RNG.uniform(0.3, 0.9)
        pos += n + int(RNG.uniform(0, 0.02) * SR)
    return stereo(out * 0.7, pan=np.repeat(RNG.uniform(-0.6, 0.6, len(out) // 2400 + 1), 2400)[:len(out)])


def swipe():
    t = t_axis(0.4)
    x = band_sweep(noise(0.4), 1000, 6000, width=0.6) * env_ad(t, 0.22, 1.6, 1.8)
    return stereo(x, pan=np.linspace(-0.5, 0.5, len(t)))


def portal():
    sec = 2.0; t = t_axis(sec); peak = 1.4
    swell = band_sweep(noise(sec), 250, 5000, width=0.9)
    swell /= np.abs(swell).max() + 1e-9
    tone = chirp(t, 110, 440, 1.0) * 0.4
    e = np.where(t < peak, (t / peak) ** 3, exp_decay(t - peak, 0.18))
    hit = np.where(t >= peak, chirp(np.maximum(t - peak, 0), 70, 35, 2.0) * exp_decay(np.maximum(t - peak, 0), 0.3), 0)
    x = (0.7 * swell + tone) * e + 0.9 * hit
    return stereo(room(soft(x, 1.4), 1.0, 0.25), width=0.35)


KIT = dict(whoosh_air=whoosh_air, whoosh_sub=whoosh_sub, boom=boom, punch=punch, odometer=odometer,
           riser=riser, shimmer=shimmer, lights_off=lights_off, key_tap=key_tap, glitch=glitch,
           swipe=swipe, portal=portal)


# ---------------------------------------------------------------- the music bed
def kick(sec=0.45):
    t = t_axis(sec)
    return chirp(t, 150, 45, 4.0) * exp_decay(t, 0.12)


def hat(sec=0.05):
    t = t_axis(sec)
    return band_sweep(noise(sec), 8000, 8000, 0.5) * exp_decay(t, 0.012)


def music(drop, bpm, length):
    n = int(length * SR); t = np.arange(n) / SR; beat = 60.0 / bpm
    out = np.zeros(n)
    # a pad: a minor chord of soft sines, quiet before the drop, fuller after
    for f in (220.0, 261.63, 329.63, 440.0):
        out += 0.06 * np.sin(2 * np.pi * f * t) * (0.7 + 0.3 * np.sin(2 * np.pi * t / (4 * beat)))
    out *= np.where(t < drop, 0.7, 1.0)
    # hats on the off-beats from the start
    h = hat()
    for k in np.arange(beat / 2, length, beat):
        a = int(k * SR); out[a:a + len(h)] += 0.12 * h[:n - a]
    # the build: a rising noise for two bars, a snare roll, then half a beat of silence
    b0 = max(0.0, drop - 8 * beat); gap = beat / 2
    bi = (t >= b0) & (t < drop - gap)
    if bi.any():
        seg = band_sweep(noise(bi.sum() / SR), 500, 6000, 0.8)
        seg /= np.abs(seg).max() + 1e-9
        out[bi] += 0.25 * seg * np.linspace(0, 1, bi.sum()) ** 2
        snare = band_sweep(noise(0.12), 1800, 1800, 1.2) * exp_decay(t_axis(0.12), 0.03)
        step = beat / 4
        for k in np.arange(drop - 4 * beat, drop - gap, step):
            a = int(k * SR); out[a:a + len(snare)] += 0.2 * snare[:n - a]
    out[(t >= drop - gap) & (t < drop)] = 0.0
    # the drop: a kick on every beat and a sub bass under it
    kk = kick()
    for k in np.arange(drop, length - beat / 2, beat):
        a = int(k * SR); out[a:a + len(kk)] += 0.9 * kk[:n - a]
    after = t >= drop
    out[after] += 0.35 * np.sin(2 * np.pi * 55.0 * t[after]) * (0.6 + 0.4 * np.sin(2 * np.pi * (t[after] - drop) / beat) ** 2)
    fade = np.clip((length - t) / 1.5, 0, 1)
    out = soft(out * fade, 1.2)
    return stereo(room(out, 1.2, 0.15), width=0.3)


def write(path, x, force):
    if os.path.exists(path) and not force:
        print(f'kept      {path} (exists; pass --force to replace it)'); return
    x = x / (np.abs(x).max() + 1e-9) * 0.89
    wf.write(path, SR, (x * 32767).astype(np.int16))
    print(f'wrote     {path}')


def main():
    global RNG
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--project', required=True, help='the same folder given to prep.py')
    ap.add_argument('--only', help='comma-separated kit names to make (default: all twelve)')
    ap.add_argument('--music', action='store_true', help='also write audio/music.wav')
    ap.add_argument('--drop-at', type=float, default=8.0, help='music only: seconds into the bed where the drop lands')
    ap.add_argument('--bpm', type=float, default=120.0, help='music only: tempo after the drop')
    ap.add_argument('--length', type=float, help='music only: bed length in seconds (default: long enough after the drop)')
    ap.add_argument('--seed', type=int, default=7, help='random seed, so a rerun makes the same sounds')
    ap.add_argument('--force', action='store_true', help='replace files that already exist')
    a = ap.parse_args()
    RNG = np.random.default_rng(a.seed)
    A = os.path.join(os.path.abspath(os.path.expanduser(a.project)), 'audio'); S = os.path.join(A, 'sfx')
    os.makedirs(S, exist_ok=True)
    names = [n.strip() for n in a.only.split(',')] if a.only else list(KIT)
    bad = [n for n in names if n not in KIT]
    if bad: sys.exit(f'Unknown kit names: {", ".join(bad)}. Known: {", ".join(KIT)}.')
    for name in names:
        write(os.path.join(S, name + '.wav'), KIT[name](), a.force)
    if a.music:
        if a.drop_at <= 2 * 60.0 / a.bpm: sys.exit('--drop-at must leave at least two beats before the drop.')
        length = a.length or max(a.drop_at + 6.0, a.drop_at / 0.75)
        if not (0.3 * length < a.drop_at < 0.8 * length):
            sys.exit(f'With --length {length:g} the drop at {a.drop_at:g} s sits outside 30 to 80 % of the bed, where '
                     'audio_prep.py looks for it. Choose another --length.')
        write(os.path.join(A, 'music.wav'), music(a.drop_at, a.bpm, length), a.force)
    print('Next: python audio_prep.py --project <dir>')


if __name__ == '__main__':
    main()
