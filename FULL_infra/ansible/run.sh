#!/bin/bash
echo root:root | /usr/sbin/chpasswd
apk update && apk upgrade
apk add ansible python openssh bkeymaps openssh bash nano iputils ircii alpine-sdk
rm -rf /var/cache/apk/* ;
mkdir -p /etc/ansible; 
echo 'localhost' > /etc/ansible/hosts
echo "nameserver 8.8.8.8" > /etc/resolv.conf
echo "nameserver 8.8.4.4" >> /etc/resolv.conf
sed -ri 's;^(root:x:0:0:root:/root:)/bin/sh;\1/bin/bash;' /etc/passwd
addgroup newuser
adduser -s /bin/bash -G newuser newuser
echo newuser:newuser | /usr/sbin/chpasswd
sed -ri 's/(wheel:x:10:root)/\1,newuser/' /etc/group
sed -ri 's/# %wheel\tALL=\(ALL\) ALL/%wheel\tALL=\(ALL\) ALL/' /etc/sudoers
su -s /bin/bash -c "git config --global user.name \"my_user\"" newuser
su -s /bin/bash -c "git config --global user.email \"my_mail@email.address\"" newuser
rc-update add sshd
sed -i 's/^#PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
sed -i 's/^#UseDNS.*/UseDNS no/' /etc/ssh/sshd_config
/etc/init.d/sshd restart
