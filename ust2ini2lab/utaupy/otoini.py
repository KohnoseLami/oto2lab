#!/usr/bin/env python3
# coding: utf-8
"""
setParam用のINIファイルとデータを扱うモジュールです。
"""
import os
import re


def main():
    """実行されたときの挙動"""
    print('耳ロボPとsetParamに卍感謝卍')


def load(path, mode='r', encoding='shift-jis'):
    """otoiniを読み取ってオブジェクト生成"""
    # otoiniファイルを読み取る
    with open(path, mode=mode, encoding=encoding) as f:
        l = [re.split('[=,]', s.strip()) for s in f.readlines()]
    # 入力ファイル末尾の空白行を除去
    while l[-1] == ['']:
        del l[-1]

    # Otoクラスオブジェクトのリストを作る
    otolist = []
    for v in l:
        oto = Oto()
        oto.from_otoini(v)
        otolist.append(oto)
    # OtoIniクラスオブジェクト化
    o = OtoIni()
    o.set_values(otolist)
    print('INIを読み取りました。: {}'.format(os.path.basename(path)))
    return o


class OtoIni:
    """oto.iniを想定したクラス"""

    def __init__(self):
        # 'Oto'クラスからなるリスト
        self.otolist = []

    def get_values(self):
        """中身を確認する"""
        return self.otolist

    def set_values(self, l):
        """中身を上書きする"""
        self.otolist = l

    def write(self, path, mode='w', encoding='shift-jis'):
        """OtoIniクラスオブジェクトをINIファイルに出力"""
        s = ''
        for oto in self.otolist:
            l = []
            l.append(oto.get_filename())
            l.append(oto.get_alies())
            l.append(oto.get_lblank())
            l.append(oto.get_fixed())
            l.append(oto.get_rblank())
            l.append(oto.get_onset())
            l.append(oto.get_overlap())
            # 数値部分を丸めてから文字列に変換
            l = l[:2] + [str(round(float(v), 3)) for v in l[2:]]
            s += '{}={},{},{},{},{},{}\n'.format(*l)  # 'l[0]=l[1],l[2],...'
        with open(path, mode=mode, encoding=encoding) as f:
            f.write(s)
        return s


class Oto:
    """oto.ini中の1モーラ"""

    def __init__(self):
        keys = ('FileName', 'Alies', 'LBlank', 'Fixed', 'RBlank', 'Onset', 'Overlap')
        l = [None] * 7
        self.d = dict(zip(keys, l))

    def from_otoini(self, l):
        """リストをもらってクラスオブジェクトにする"""
        keys = ('FileName', 'Alies', 'LBlank', 'Fixed', 'RBlank', 'Onset', 'Overlap')
        # 数値部分をfloatにする
        l = l[:2] + [float(v) for v in l[2:]]
        self.d = dict(zip(keys, l))
        return self

    # ここからノートの全値の処理----------------------
    def get_values(self):
        """中身を確認する"""
        return self.d

    def set_values(self, d):
        """中身を上書きする"""
        self.d = d
    # ここまでノートの全値の処理----------------------

    # ここからノートの各値の参照----------------------
    def get_filename(self):
        """wavファイル名を確認する"""
        return self.d['FileName']

    def get_alies(self):
        """エイリアスを確認する"""
        return self.d['Alies']

    def get_lblank(self):
        """左ブランクを確認する"""
        return self.d['LBlank']

    def get_fixed(self):
        """固定範囲を確認する"""
        return self.d['Fixed']

    def get_rblank(self):
        """右ブランクを確認する"""
        return self.d['RBlank']

    def get_onset(self):
        """先行発声を確認する"""
        return self.d['Onset']

    def get_overlap(self):
        """右ブランクを確認する"""
        return self.d['Overlap']
    # ここまでノートの各値の参照----------------------

    # ここからの各値の上書き----------------------
    def set_filename(self, x):
        """wavファイル名を上書きする"""
        self.d['FileName'] = x

    def set_alies(self, x):
        """エイリアスを上書きする"""
        self.d['Alies'] = x

    def set_lblank(self, x):
        """左ブランクを上書きする"""
        self.d['LBlank'] = x

    def set_fixed(self, x):
        """固定範囲を上書きする"""
        self.d['Fixed'] = x

    def set_rblank(self, x):
        """右ブランクを上書きする"""
        self.d['RBlank'] = x

    def set_onset(self, x):
        """先行発声を上書きする"""
        self.d['Onset'] = x

    def set_overlap(self, x):
        """右ブランクを上書きする"""
        self.d['Overlap'] = x
    # ここまでノートの各値の上書き----------------------


if __name__ == '__main__':
    main()

if __name__ == '__init__':
    pass
