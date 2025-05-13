# Focus Blocker

A CLI tool to block distracting websites using the NextDNS API, with lockout logic to prevent easy reversal.

## Setup

> [!TIP]
> In order for this tool to work, the following setup steps are required.

1. Create a NextDNS account and [a new profile](apple.nextdns.io) for your iPhone.

2. Download and install this new configuration profile on your iPhone (you’ll need to allow it in Settings > General > VPN & Device Management).

> By downloading the `.mobileconfig` file and clicking on it on your iPhone, you'll see a prompt to navigate to Settings and install the profile. 

> This gives your iPhone persistent access to the custom DNS settings — including the denylist your Python script manages.

3. Navigate to your NextDNS account page, and generate a new [API key](https://my.nextdns.io/account).

4. Create a new `.env` file at the root of the directory, referring to the `.env.example` template, and make sure to input your newly generated `NEXTDNS_API_KEY` and `NEXTDNS_PROFILE_ID`.
