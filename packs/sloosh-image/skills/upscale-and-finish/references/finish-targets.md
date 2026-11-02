# Finish targets

Use these tables to pick the factor, the enhancement mode and the file format. The Space form and the quote decide what is possible. If they differ from this file, follow them.

## Pixel size from the use case

Pixel size equals the print size in inches times the dots per inch (dpi). Pick the smallest factor that reaches the target long side. The output size is the source size times the factor, so 2048 px at 2x gives 4096 px. For exact pixel dimensions, the user resizes after download.

| Use case | Target long side | Usual factor from a 2K source |
|---|---|---|
| Social post or story | About 1080 to 1920 px | None. Do not upscale. |
| Web hero or banner | About 2560 to 3840 px | 2x |
| 4K screen | 3840 px | 2x |
| A4 print at 300 dpi | About 3500 px | 2x |
| A3 print at 300 dpi | About 5000 px | 4x |
| A2 print at 300 dpi | About 7000 px | 4x |
| Large banner, such as 6 by 4 feet at 100 dpi | About 7200 px | 4x, or 6x from a small source |
| Billboard or outdoor | Depends on the printer | 4x. Viewing distance hides the rest. |
| Packaging proof | Print size at 300 dpi | 2x with the most faithful mode |

- Ask the printer for the dpi when the user has a print spec. Large-format prints often need 100 to 150 dpi, not 300.
- Run one upscale per image. If the target needs more than the largest factor the Space allows, tell the user the largest size this skill can make.
- An upscale keeps the aspect ratio. For exact pixel dimensions in a new ratio, reframe first.

## Enhancement mode from the source

Use this table only when the Space form offers a mode field. Match the labels in the form to these kinds of modes. Use a colour or tone field only when the user asks for it.

| Source | Choose |
|---|---|
| Clean AI render of a product | The standard mode, 2x or 4x |
| Soft or low-resolution photo | The low-resolution mode |
| Text or a user interface in the image | The text mode |
| 3D render or illustration | The illustration or CGI mode |
| Real people | Face enhancement on, any creativity field at its lowest |
| Nothing may change, such as a packaging proof | The most faithful mode, 2x |

## File format

| Use | Format |
|---|---|
| Web, social or email | JPG |
| Print, packaging or a proof | PNG |
| An image with a transparent background | PNG |

If the Space form has no format field, tell the user which format they get.

## Delivery note

Give the user one line per image: the pixel size (the source size times the factor), the factor, the enhancement mode and the format. Name the file from the idempotency key, such as image-serum-hero-4x5-up4x-v1.
