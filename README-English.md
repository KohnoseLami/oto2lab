# oto2lab

A software which can convert UST to INI (for setParam), INI to LAB.

Using this software, you can to phoneme-labeling of song wav files.

THE BELOW IS TRANSLATED TEXT FROM JAPANESE README USING "[MiraiTransrate](https://miraitranslate.com/trial/)".

## Purpose

To make singing DB by utilizing existing software (setParam) and know-how (Otoining) around UTAU, and of UTAU-users.

## Notes

- Please note that the script name may change with the upgrade.

## Development Environment

- Windows 10
- Python 3.8

## Procedure (Entire)

The specification has changed after v2.0.0.

1. Sing to make a WAV file.
1. Make UST of the song.
1. Match the timing of WAV to UST.
1. Convert UST to INI with **oto2lab**.
1. Edit the INI with **setParam** and save it.
1. Convert to LAB with **oto2lab**.
1. Finished

## Procedure (Details)

### Phonome-labeling with SetParam

For the purpose of label conversion, it is used differently from the original sound setting of UTAU.
Set the following.

- Offset: Not used
- Overlap: Consonant start
- Preutterance: Vowel start
- Consonant: Not used (the boundary between the second and third notes only when composed of three phonemes)
- Cutoff: Not used

### How to use this tool

1. Double-click oto2lab.exe to launch.
1. Select mode according to display. (*NOTE: So sorry, CLI text is only in Japanese.*)
1. Drag and drop the file you want to process to the displayed screen.
1. Next to the file you want to process is the converted file.