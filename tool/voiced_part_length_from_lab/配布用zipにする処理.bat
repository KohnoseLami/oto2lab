REM reclsit2region.py��exe�ɂ��Ĕz�z�pzip�ɂ���o�b�`

mkdir �̏�DB�̗L�������Ԃ𒲂ׂ�c�[��
copy /Y voiced_part_length_from_lab.py �̏�DB�̗L�������Ԃ𒲂ׂ�c�[��\voiced_part_length_from_lab.py
copy /Y README.md �̏�DB�̗L�������Ԃ𒲂ׂ�c�[��\readme.txt
cd �̏�DB�̗L�������Ԃ𒲂ׂ�c�[��

pyinstaller.exe voiced_part_length_from_lab.py --onefile --clean --exclude-module readme.txt

move /Y dist\voiced_part_length_from_lab.exe voiced_part_length_from_lab.exe
rmdir /s /q dist, build, __pycache__
del /q voiced_part_length_from_lab.spec, voiced_part_length_from_lab.py
cd ..

powershell compress-archive -Force �̏�DB�̗L�������Ԃ𒲂ׂ�c�[�� �̏�DB�̗L�������Ԃ𒲂ׂ�c�[��.zip
rmdir /s /q �̏�DB�̗L�������Ԃ𒲂ׂ�c�[��
