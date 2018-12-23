**change log**
1. **0.0.0 (Active)**
    -stable version

2. **0.1.0 (Future)**
    -save passwords to file.
    -send passwords to email.
    -generate passwords without conflicts between flags order.

**install**
pip install clipass

**help**
clipass -h

**developers**
1. you can add your own flags, by adding them to the "models" folder (each flag will be a package)
2. you can take a loog for a reference to your own flag model inside "core/base_flags/length"

**examples**
clipass >> generates 16 random passwords, with 10 chars
clipass -m 2 >> generates 2 random passwords, with 10 chars
clipass -l 5 >> generates 16 random password, with 5 chars