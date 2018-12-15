# Raspberry-Pi

## switchbot_timer.py
```bash
# Bluetoothの機種(Macアドレス)一覧を表示
sudo hcitool lescan
# Macアドレスをテスト
python switchbot_timer.py --test <Macアドレス>
# タイマーセット
nohup python switchbot_timer.py <タイマーインターバル[分]> <Macアドレス> > /dev/null &
```
