# Raspberry-Pi

## SwitchBotTimer
```bash
# Bluetoothの機種(Macアドレス)一覧を表示
sudo hcitool lescan

# Macアドレスをテスト
python check_address.py <Macアドレス>

# Macアドレスと実行間隔をファイルに追記

# 既存プロセスをkill
ps aux | grep python
kill <PID>

# タイマーセット
python set_timer.py
```
