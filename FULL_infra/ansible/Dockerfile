FROM alpine:3.7

RUN echo root:root | /usr/sbin/chpasswd
RUN apk update && apk upgrade
RUN apk add ansible python openssh openssh bash iputils openrc 
RUN rc-update add sshd
RUN mkdir -p /etc/ansible; 
RUN echo 'localhost' > /etc/ansible/hosts
RUN echo "nameserver 8.8.8.8" > /etc/resolv.conf
RUN echo "nameserver 8.8.4.4" >> /etc/resolv.conf
RUN sed -ri 's;^(root:x:0:0:root:/root:)/bin/sh;\1/bin/bash;' /etc/passwd
#RUN addgroup newuser
#RUN adduser -s /bin/bash -G newuser newuser
#RUN echo newuser:newuser | /usr/sbin/chpasswd
#RUN sed -ri 's/(wheel:x:10:root)/\1,newuser/' /etc/group
#RUN sed -ri 's/# %wheel\tALL=\(ALL\) ALL/%wheel\tALL=\(ALL\) ALL/' /etc/sudoers
#RUN su -s /bin/bash -c "git config --global user.name \"my_user\"" newuser
#RUN su -s /bin/bash -c "git config --global user.email \"my_mail@email.address\"" newuser
RUN sed -i 's/^#PermitRootLogin.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -i 's/^#UseDNS.*/UseDNS no/' /etc/ssh/sshd_config

#RUN rm -rf /var/cache/apk/* ;

EXPOSE 22
#ENTRYPOINT ["/run.sh"]
