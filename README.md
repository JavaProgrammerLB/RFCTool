# RFCTool
For explore RFC documents

#### rfc_downloader.py  
- suport python3
- request **requests**
- update shebang in line one, mine is:
```python
#!/usr/local/bin/python3
```

change to your pytho3's path,such as:
```python
#!/usr/local/python
```

- Usage  
```shell
./rfc_downloader.py [rfc_number]
```

- Add Executable permissions
```shell
sudo chmod +x rfc_downloader.py
```

- Example
Download RFC7540 with:
```shell
./rfc_downloader.py 7540
```
