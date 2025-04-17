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