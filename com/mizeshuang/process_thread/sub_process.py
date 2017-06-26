# 子进程
import subprocess
print('$ nslookup www.baidu.com')
r = subprocess.call(['nslookup', 'www.baidu.com'])
print('Exit code:', r)

# 如果子进程还需要输入，则使用subprocess的communicate()方法
print('$ nslookup ')
p = subprocess.Popen(['nslookup'], stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE)
output, err = p.communicate(b'set q=mx\nbaidu.com\nexit\n')
print(output.decode('utf-8'))
print('Exit code:',p.returncode)