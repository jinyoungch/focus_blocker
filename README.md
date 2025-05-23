# Focus Blocker

A CLI tool to block distracting websites using the NextDNS API, with lockout logic to prevent easy reversal.

## Setup

> [!NOTE]
> In order for this tool to work, the following setup steps are required.

1. Create a [NextDNS account](https://my.nextdns.io/) and a new [Apple Configuration Profile](apple.nextdns.io) for your iPhone.

2. Download and install this new configuration profile on your iPhone.

> By downloading the `.mobileconfig` file and clicking on it on your iPhone, you'll see a prompt to navigate to `Settings > General > VPN & Device Management` and install the profile.

3. Navigate to your [NextDNS account](https://my.nextdns.io/account) page, and generate a new API key at the bottom of the page.

4. Create a new `.env` file at the root of the directory, referring to the `.env.example` template, and make sure to input your newly generated `NEXTDNS_API_KEY` and `NEXTDNS_PROFILE_ID`.

5. In your terminal, navigate to the root of this directory and install the following dependencies:

```
pip install python-dotenv requests
```

## Usage

The following are the sample commands that are supported by this CLI:

```bash
python cli.py add youtube.com
python cli.py remove facebook.com
python cli.py push --lockout 48
python cli.py status
```

> [!TIP]
> In order to use this CLI more ergonomically, you can set up an alias in your terminal, eg. by adding the following line to `~/.zshrc`:

```zsh
alias focusblock="python focus_blocker/cli.py"
```

That way you can run the above commands as:

```zsh
focusblock add youtube.com
focusblock remove facebook.com
focusblock push --lockout 48
focusblock status
```