# ehids安装
##前置安装

```
UBUNTU 21.04 server
go version go1.17.2 linux/amd64
Ubuntu clang version 12.0.0-3ubuntu1~21.04.2
openjdk version "1.8.0_292"
```

note: module requires Go 1.16
所以需要安装go 1.16以上
```
sudo add-apt-repository ppa:longsleep/golang-backports
sudo apt update
sudo apt install golang-go
```
## 安装步骤
```
sudo apt-get install -y make gcc libssl-dev bc libelf-dev libcap-dev clang gcc-multilib llvm libncurses5-dev git pkg-config libmnl-dev bison flex graphviz
sudo apt-get install -y make gcc clang llvm git pkg-config dpkg-dev gcc-multilib
cd ~/download/
sudo apt update
sudo apt-get source linux-image-$(uname -r)
sudo apt-get source linux-image-unsigned-$(uname -r)
sudo apt install libbfd-dev libcap-dev zlib1g-dev libelf-dev libssl-dev
```

设置代理
```
go env -w GOPROXY=https://goproxy.io,direct
go env -w GO111MODULE=on
```

## 编译运行
```
git clone https://github.com/ehids/ehids-agent.git
cd ehids
make
./bin/ehids-agent
```

## 另开shell运行
```
cd examples
javac Main.java
java Main
```

注： Ubuntu20.04
```
 couldn't init manager: error:map ringbuf_proc: map create without BTF: invalid argument , couldn't load eBPF programs, cs:&{map[ringbuf_proc:RingBuf(keySize=0, valueSize=0, maxEntries=16777216, flags=0)] map[kretprobe_copy_process:0xc0010dd0e0] LittleEndian}

```