# mbwrapper

A Python3 wrapper for the MalwareBazaar API.

## Usage

```python
>>> import mbwrapper as mw
>>> info = mw.get_info("7338b335ad5471cb67658f27836374f0") # Accepts SHA256, MD5 or SHA1 hashes.
>>> info["query_status"]
'ok'
>>> sha256 = info["sha256_hash"]
>>> sha256
'e167b20f1acf48f7ce0ae33a218e2c1b300b41c012ededf03e7a3522a4ebe95e'
>>> zipfile = mw.get_file(sha256) # Accepts only SHA256 values.
>>> zipfile[:16] # Byte string containing the compressed file.
b'PK\x03\x043\x00\x03\x00c\x00\xaa\x89\x81TD\x8c'
>>>
>>> # To decompress the file in-memory, use `io` and `pyzipper` like so:
>>> import io
>>> import pyzipper as pz
>>> fileobj = io.BytesIO(zipfile)    # Convert the byte string into a file-like object.
>>> zipfile = pz.AESZipFile(fileobj) # Open with pyzipper.
>>> zipfile.setpassword(b"infected") # All MalwareBazaar samples use this password.
>>> unzipped = zipfile.read(
...     zipfile.filelist[0] # Decompress the first file in the archive.
... )
>>> len(unzipped)
145408
>>> unzipped[:16]
b'MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00'
>>> # Now the `unzipped` byte string contains the decompressed malware sample.
```

## Developers

To work on `mbwrapper`, you'll need to install the dev requirements:

* `pip install -r dev_requirements.txt`

Use the `lint.sh` script to help keep code clean and readable.