# MyFHE
これは、セキュリティ・キャンプ2020L-Ⅱトラックで学んだ内容を実装するためのリポジトリです。(un-completed)
TFHEの実装を進めています。
TLWE->TRLWE->TRGWS->CMUX->BlindRotate->IdentityKeySwitch->HomNANDと実装を進めていく予定です。
現状CMUXまで実装が終わっています。

offsetによる最適化は実装できていません。FFTはあまり理解できていないので今のところは講師のプログラムのコピーです。

## How To Run

TRGSWまでのテスト確認は出来ているのですが、パラメータ調節を行っていないためTRLWEのテストコードまでしか載せていません。
'''
python3 tlweenc.py
'''

と実行すればTLWEのテストコードが実行されます。

## 今後の予定
HomNANDまでの実装を年内に行う予定です。
パラメータ調整も年内にできれば良いと思っていますが、厳しいかもしれません。

参考url:
https://nindanaoto.github.io
