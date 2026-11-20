# Uploading files

| Where the file is | Route |
| --- | --- |
| Public HTTP(S) URL | `upload_file_from_url` |
| Attached to the chat | Send it from your code environment (below) |
| On the user's computer | Point to the history card's **Upload a file…** button |

Never ask for or use a Galaxy API key; the upload address authorizes the bytes.

Set the datatype the tutorial or tool expects (for example `ome.tiff`) rather than a generic one.

## A chat attachment

1. Call `start_file_upload` with `historyId`, `fileName` and the file's exact `size` in bytes.
2. Send the file to `upload.url` with the code below, in chunks of `upload.chunk_bytes`.
3. Call `finish_file_upload` with the returned `session_id`, then `wait_for_datasets` until the dataset is ready.

```python
import os, urllib.request

def send(path, url, chunk_bytes):
    size, offset = os.path.getsize(path), 0
    with open(path, "rb") as f:
        while offset < size:
            req = urllib.request.Request(url, data=f.read(chunk_bytes), method="PATCH", headers={
                "Tus-Resumable": "1.0.0",
                "Content-Type": "application/offset+octet-stream",
                "Upload-Offset": str(offset),
            })
            with urllib.request.urlopen(req, timeout=300) as resp:
                offset = int(resp.headers["Upload-Offset"])
```

If the request cannot reach the Galaxy site, stop and point to the card's Upload button. Upload several files one at a time and report each result.

## A file the user uploaded with the card

When the user refers to a file they just uploaded, use `last_upload` from the card's context if present. Otherwise re-read that history, newest first, and match the file name. Ask if the name matches several datasets or none, and use `wait_for_datasets` until it is ready before running a tool on it.
