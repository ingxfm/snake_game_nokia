# Run the code in the linux container

install Podman

```
[root@3c531e95770c /]# dnf install -y --quiet podman

Upgraded:
  systemd-libs-248.10-1.fc34.x86_64
Installed:
  acl-2.3.1-1.fc34.x86_64                                  catatonit-0.1.7-1.fc34.x86_64                     conmon-2:2.0.32-1.fc34.x86_64
  containernetworking-plugins-1.0.1-1.fc34.x86_64          containers-common-4:1-21.fc34.noarch              criu-3.16.1-2.fc34.x86_64
  criu-libs-3.16.1-2.fc34.x86_64                           crun-1.4.2-1.fc34.x86_64                          cryptsetup-libs-2.3.7-1.fc34.x86_64
  dbus-1:1.12.20-3.fc34.x86_64                             dbus-broker-29-2.fc34.x86_64                      dbus-common-1:1.12.20-3.fc34.noarch
  dbus-libs-1:1.12.20-3.fc34.x86_64                        device-mapper-1.02.175-1.fc34.x86_64              device-mapper-libs-1.02.175-1.fc34.x86_64
  diffutils-3.7-8.fc34.x86_64                              dnsmasq-2.86-4.fc34.x86_64                        fuse-common-3.10.4-1.fc34.x86_64
  fuse-overlayfs-1.7.1-2.fc34.x86_64                       fuse3-3.10.4-1.fc34.x86_64                        fuse3-libs-3.10.4-1.fc34.x86_64
  iptables-legacy-1.8.7-8.fc34.x86_64                      iptables-legacy-libs-1.8.7-8.fc34.x86_64          iptables-libs-1.8.7-8.fc34.x86_64
  jansson-2.13.1-2.fc34.x86_64                             kmod-29-2.fc34.x86_64                             kmod-libs-29-2.fc34.x86_64
  libargon2-20171227-6.fc34.x86_64                         libbpf-2:0.4.0-1.fc34.x86_64                      libbsd-0.10.0-7.fc34.x86_64
  libibverbs-37.2-2.fc34.x86_64                            libmnl-1.0.4-13.fc34.x86_64                       libnet-1.2-2.fc34.x86_64
  libnetfilter_conntrack-1.0.8-2.fc34.x86_64               libnfnetlink-1.0.1-19.fc34.x86_64                 libnftnl-1.1.9-2.fc34.x86_64
  libnl3-3.5.0-6.fc34.x86_64                               libpcap-14:1.10.1-1.fc34.x86_64                   libseccomp-2.5.3-1.fc34.x86_64
  libslirp-4.4.0-4.fc34.x86_64                             libxkbcommon-1.3.0-1.fc34.x86_64                  nftables-1:0.9.8-3.fc34.x86_64
  podman-3:3.4.4-1.fc34.x86_64                             podman-gvproxy-3:3.4.4-1.fc34.x86_64              podman-plugins-3:3.4.4-1.fc34.x86_64
  protobuf-c-1.3.3-7.fc34.x86_64                           qrencode-libs-4.1.1-1.fc34.x86_64                 slirp4netns-1.1.12-2.fc34.x86_64
  systemd-248.10-1.fc34.x86_64                             systemd-networkd-248.10-1.fc34.x86_64             systemd-pam-248.10-1.fc34.x86_64
  systemd-rpm-macros-248.10-1.fc34.noarch                  xkeyboard-config-2.33-1.fc34.noarch               yajl-2.1.0-16.fc34.x86_64

[root@3c531e95770c /]#
```

install vncviewer (as a part of the TigerVNC)

```
[root@3c531e95770c /]# dnf install -y --quiet tigervnc

Installed:
  fltk-1.3.8-1.fc34.x86_64
  fontconfig-2.13.94-2.fc34.x86_64
  freetype-2.10.4-3.fc34.x86_64
  graphite2-1.3.14-7.fc34.x86_64
  harfbuzz-2.7.4-3.fc34.x86_64
  hicolor-icon-theme-0.17-10.fc34.noarch
  hwdata-0.356-1.fc34.noarch
  libX11-1.7.2-3.fc34.x86_64
  libX11-common-1.7.2-3.fc34.noarch
  libX11-xcb-1.7.2-3.fc34.x86_64
  libXau-1.0.9-6.fc34.x86_64
  libXcursor-1.2.0-5.fc34.x86_64
  libXext-1.3.4-6.fc34.x86_64
  libXfixes-6.0.0-1.fc34.x86_64
  libXft-2.3.3-6.fc34.x86_64
  libXi-1.7.10-6.fc34.x86_64
  libXinerama-1.1.4-8.fc34.x86_64
  libXrender-0.9.10-14.fc34.x86_64
  libXxf86vm-1.1.4-16.fc34.x86_64
  libdrm-2.4.109-1.fc34.x86_64
  libglvnd-1:1.3.3-1.fc34.x86_64
  libglvnd-glx-1:1.3.3-1.fc34.x86_64
  libjpeg-turbo-2.0.90-3.fc34.x86_64
  libpciaccess-0.16-4.fc34.x86_64
  libpng-2:1.6.37-10.fc34.x86_64
  libxcb-1.13.1-7.fc34.x86_64
  libxshmfence-1.3-8.fc34.x86_64
  mesa-libGL-21.1.8-3.fc34.x86_64
  mesa-libglapi-21.1.8-3.fc34.x86_64
  pixman-0.40.0-3.fc34.x86_64
  tigervnc-1.12.0-4.fc34.x86_64
  tigervnc-icons-1.12.0-4.fc34.noarch
  tigervnc-license-1.12.0-4.fc34.noarch
  xml-common-0.6.3-56.fc34.noarch

[root@3c531e95770c /]#
```

Build the container image
```
  snake_game_nokia git:(main) ✗ podman build .
STEP 1/7: FROM ubuntu
STEP 2/7: RUN apt-get update && apt-get install -y python3 x11vnc xvfb python3-tk
--> Using cache 0e939d629a9b91a978345041247e7bff204575233b0a4ea81db2c4c2a1a95322
--> 0e939d629a9
STEP 3/7: RUN mkdir ~/.vnc
--> Using cache a179bc69533e050cc52ede22db63e024c8c05d545ebd74fc08727d6a94e5a37a
--> a179bc69533
STEP 4/7: RUN x11vnc -storepasswd 1234 ~/.vnc/passwd
--> Using cache a3a00e9e49cfbfd52dcbd3027e0ca493a52ca7eff5c34e0b19679fcb106abce9
--> a3a00e9e49c
STEP 5/7: RUN bash -c 'echo "cd /code && python3 main.py" >> /.bashrc'
--> Using cache 7198702e9d804b4fdb38eff4b6809e3158cb2443a73cdf7361bf622111d7497e
--> 7198702e9d8
STEP 6/7: ENV HOME=/
--> Using cache 9ff33304e574b469d40fe0407ac4c55dcc6b75325b655b3a80e593b19612ca5b
--> 9ff33304e57
STEP 7/7: CMD x11vnc -forever -usepw -create
--> Using cache f66c9fce8a1a6098abf500f683d23a6d3d924dc612d36c3cb68c1f0878fc88d9
--> f66c9fce8a1
f66c9fce8a1a6098abf500f683d23a6d3d924dc612d36c3cb68c1f0878fc88d9
```

run the container, select password for communication with the vnc server
running in the container
➜  snake_game_nokia git:(main) ✗ podman run -it -p5900:5900 -v .:/code:Z f66c9fce8a1
Enter VNC password:
Verify password:
Write password to //.vnc/passwd?  [y]/n
Password written to: //.vnc/passwd
21/02/2022 16:30:42 x11vnc version: 0.9.16 lastmod: 2019-01-05  pid: 7
21/02/2022 16:30:42
21/02/2022 16:30:42 wait_for_client: WAIT:cmd=FINDCREATEDISPLAY-Xvfb
21/02/2022 16:30:42
21/02/2022 16:30:42 initialize_screen: fb_depth/fb_bpp/fb_Bpl 24/32/2560
21/02/2022 16:30:42
21/02/2022 16:30:42 Autoprobing TCP port
21/02/2022 16:30:42 Autoprobing selected TCP port 5900
21/02/2022 16:30:42 Autoprobing TCP6 port
21/02/2022 16:30:42 Autoprobing selected TCP6 port 5900
21/02/2022 16:30:42 listen6: bind: Address already in use
21/02/2022 16:30:42 Not listening on IPv6 interface.
21/02/2022 16:30:42

The VNC desktop is:      5ebe80008c77:0
PORT=5900

---
**NOTE** The `-p5900:5900` makes the port 5900 in the container available outside as 5900
**NOTE** The `-v .:/code:Z` makes the code of the project (the actual working 
directory) available inside of the container for RW. Do you see the
possibility for the attacker (a mallicious person who sent the commit we want
to test) to compromise our code?

From another terminal, run

```
➜  vncviewer localhost:5900
```

Answer the password prompt and play the game over vnc.
