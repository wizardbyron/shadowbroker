# Shadowbroker

Shadowbroker helps you to create a [Shadowsocks](https://shadowsocks.org/) server on Cloud/VPS.

## Setup Shadowsocks server on AWS via Cloudformation

Please make sure you have `awscli` installed and setup awscli with `aws configure`.

Create a new stack for shadowsocks server:

``` shell
git clone https://github.com/wizardbyron/shadowbroker.git
cd shadowbroker
aws cloudformation deploy --template-file ./aws/cloudformation/shadowzone.yaml --stack-name shadowzone
```

Then you will have a new cloudformation stack named "shadowzone", and it will export the server IP from:

``` shell
aws cloudformation list-exports
```

You can get dynamic IP of your instance in the outputs.

NOTE: The default port is `8388`, default password is `password` and the encrypt with `aes-256-cfb` and you can update them in aws/cloudformation/shadowzone.yaml

## LICENSE

See [LICENSE](./LICENSE)