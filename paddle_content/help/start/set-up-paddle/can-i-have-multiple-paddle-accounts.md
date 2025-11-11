---
title: "Can I have multiple Paddle accounts? - Help Center - Paddle"
description: "This is up to you  and it depends on what you need. Read more about then options here."
source: "help/start/set-up-paddle/can-i-have-multiple-paddle-accounts.html"
---

# Can I have multiple Paddle accounts? - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[Start](/help/start)[Set up Paddle](/help/start/set-up-paddle)

Can I have multiple Paddle accounts?

**Do I need one Paddle account for each of my websites?**

This is up to you - and it depends on your needs

**One account for all businesses  
** You can sell all your products and services from one Paddle account, but please note that some settings are global for the whole account and can’t be customized to individual products.

Per account, it is only possible to set:

  * one legal name
  * one display name
  * one tax setting (tax added or included in price) in Paddle Classic. This can be customized by individual prices in Paddle Billing
  * one bank statement descriptor
  * one set of metrics and reporting data


That being said, you can use the ['referring_domain' (Paddle Classic)](https://developer.paddle.com/reference/5e0171ec215eb-checkout-parameters?_gl=1*fnasfs*_gcl_au*NTg5MzE5ODU4LjE3MjYxMzc0MzQuMTEwNzE5MjkzNi4xNzI5NTg5OTI0LjE3Mjk1ODk5MjQ.*_ga*MTU4MjU3Nzc4MC4xNzA5NzQyMDY2*_ga_9XVE7HZLLZ*MTcyOTYwNjYyMS4zMzIuMS4xNzI5NjA2Njc4LjMuMC4w#:~:text=%3C%3D%201000%20characters-,referring_domain,-string) or the ['customData' (Paddle Billing)](https://developer.paddle.com/paddlejs/methods/paddle-checkout-open#:~:text=or%20discountId.-,customData,-object%20or%20null) parameter in the Paddle.js implementation to record which website a sale originates from. This data will then be included in webhook alerts and reporting so that you can filter by this later if this is sufficient for you.

TL;DR - yes you can, but this might make it tricky to keep your businesses separate in reporting and accounting.

**Separate accounts for each business  
** This option will make it easier for you to keep the data from each business separate, and to have different settings for the various businesses. The only downside to this is that you will need to create a new account with a unique email address for every new business.

TL;DR - a tidier and flexible option, but it necessitates maintaining two separate accounts.