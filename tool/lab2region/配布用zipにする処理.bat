REM reclsit2region.py��exe�ɂ��Ĕz�z�pzip�ɂ���o�b�`

mkdir ���f���x�����烊�[�W����CSV�𐶐�����c�[��
copy /Y lab2region.py ���f���x�����烊�[�W����CSV�𐶐�����c�[��\lab2region.py
copy /Y README.md ���f���x�����烊�[�W����CSV�𐶐�����c�[��\readme.txt
cd ���f���x�����烊�[�W����CSV�𐶐�����c�[��

pyinstaller.exe lab2region.py --onefile --clean --exclude-module readme.txt

move /Y dist\lab2region.exe lab2region.exe
rmdir /s /q dist, build, __pycache__
del /q lab2region.spec, lab2region.py
cd ..

powershell compress-archive -Force ���f���x�����烊�[�W����CSV�𐶐�����c�[�� ���f���x�����烊�[�W����CSV�𐶐�����c�[��.zip
rmdir /s /q ���f���x�����烊�[�W����CSV�𐶐�����c�[��
