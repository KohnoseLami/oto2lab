REM reclsit2region.py��exe�ɂ��Ĕz�z�pzip�ɂ���o�b�`

mkdir UST��BPM�Ɖ�����擾����c�[��
copy /Y ust_bpm_and_range.py UST��BPM�Ɖ�����擾����c�[��\ust_bpm_and_range.py
copy /Y README.md UST��BPM�Ɖ�����擾����c�[��\readme.txt
cd UST��BPM�Ɖ�����擾����c�[��

pyinstaller.exe ust_bpm_and_range.py --onefile --clean --exclude-module readme.txt

move /Y dist\ust_bpm_and_range.exe ust_bpm_and_range.exe
rmdir /s /q dist, build, __pycache__
del /q ust_bpm_and_range.spec, ust_bpm_and_range.py
cd ..

powershell compress-archive -Force UST��BPM�Ɖ�����擾����c�[�� UST��BPM�Ɖ�����擾����c�[��.zip
rmdir /s /q UST��BPM�Ɖ�����擾����c�[��
