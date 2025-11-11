---
title: "What is Audience? - Help Center - Paddle"
description: "The  Audience  area of our dashboard is a comprehensive list of your buyers that have optedin to receive marketing communication from you  Youre able to togg"
source: "help/manage/your-customers/what-is-audience.html"
---

# What is Audience? - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[Manage](/help/manage)[Your customers](/help/manage/your-customers)

What is Audience?

_This is only applicable to Paddle Classic_

The [Audience](https://vendors.paddle.com/audience) area of our dashboard is a comprehensive list of your buyers that have opted-in to receive marketing communication from you.

You’re able to toggle the Audience collection on/off in your [Checkout Settings](https://vendors.paddle.com/checkout-settings).

If you have Audience collection enabled, buyers can be added to Audience in several different ways;

  * After entering their email address during the checkout process.
  * Using the [Audience pop-up](https://developer.paddle.com/guides/21436bcf0a110-paddle-audience#audience-popups--prompts) to collect an email address.
  * Using the [Audience Add API](https://developer.paddle.com/guides/21436bcf0a110-paddle-audience#direct-api).


When purchasing buyers will need to opt-in to receive marketing communications from you. This is as a result of the roll-out of the [GDPR](https://paddle.com/blog/rolling-out-gdpr). Only those who have opted in will appear under Audience. Whereas all customers will appear in your Transaction reports.

If you are already collecting the email address yourself (to use with our Audience API, or to skip the first step of the checkout), you can pass the consent to us using `marketing_consent: true` in your implementation.

Currently, you’re able to export all customer data from the Audience area, then import this into a mailing provider of your choice.

For more advice on how to collect buyer email addresses and communicate with them in a compliant way, [please get in touch](mailto:sellers@paddle.com).