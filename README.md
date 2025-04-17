# zenodo_spoof
Archive release after zenodo integration

## Steps taken to reproduce behavior:

1. Created GitHub repository
- https://github.com/ibaumgart/zenodo_spoof

2. Created Zenodo account

3. Linked personal GitHub repository in Zenodo
- https://zenodo.org/account/settings/github/

4. Enabled this GitHub repo archiving in Zenodo account
- https://zenodo.org/account/settings/github/
- zenodo_spoof set to enabled

5. Made a release commit
- Added Release_0.txt
- Commited/pushed to repo

6. Added release tag in a new commit
- git tag v0
- git push origin v0

7. In GitHub created this as release v0 using tag v0

8. Confirmed that Zenodo archived v0

9. DISABLED Zenodo archiving for zenodo_spoof GitHub

10. Added files for next release
- .zenodo.json with my details
- Release_1.txt
- Edited README.md steps

11. Made a release commit
- Added files
- Committed/pushed to repo
- Added release tag for v1

12. Confirmed that release v1 was NOT archived in Zenodo

13. Re-ENABLED zenodo_spoof GitHub repo in Zenodo

14. Added zenodo_spoof.py
- Code used to re-send the webhook request for Zenodo archiving of a previous release
- Taken from https://github.com/zenodo/zenodo/issues/1463#issuecomment-1034581344
- *NOTE*: Zenodo will always use the latest webhook as the latest release on Zenodo page. Therefore, you must use this code in chronological order: oldest to newest.
- *NOTE*: I did not commit the actual script I used to send the webhook, just the template.

15. Ran zenodo_spoof_v1.py
- This had the appropriate values filled out for this repository
```
PS D:\iwb5\Git\zenodo_spoof> python zenodo_spoof_v1.py
<Response [202]>
```
- Response 202 indicates success

16. Zenodo failed to archive event, but has a log for the request
```
{
    "error_id": "86ed0c2e3cf5439380d62b309b2cf589",
    "errors": "Extra metadata load failed."
}
```
17. Tried deleting release and re-releasing with same tag and metadata
- Same error from Zenodo

18. Problem lies with .zenodo.json
- Unexpected format or structure probably
- Switching to alternate CITATION.cff
- Offers pre-commit hook to validate

19. Committed CITATION.cff as release v2
- New Zenodo error
```
{
    "error_id": "baa6bae408714235b9b69e6d880d537e",
    "errors": "Citation metadata load failed"
}
```

20. Downloaded cff-convert
- https://github.com/citation-file-format/cffconvert
- Problem with "N/A" value for "license" field, must be specific type

21. cff does not allow separate "author" and "contributor" fields, switched back to .zenodo.json

22. Added .zenodo.json back to repo

23. Installed check-jsonschema and checked .zenodo.json
- pip install check-jsonschema
```
PS D:\iwb5\Git\zenodo_spoof> check-jsonschema --schemafile https://raw.githubusercontent.com/zenodo/zenodo/refs/heads/master/zenodo/modules/deposit/jsonschemas/deposits/records/legacyrecord.json .zenodo.json
ok -- validation done
```

24. Committed and added as tag v4, released via GitHub

25. Zenodo failed again
```
{
    "error_id": "8b3b2ecef4534db2b9c318eb58076588",
    "errors": "Extra metadata load failed."
}
```

26. 