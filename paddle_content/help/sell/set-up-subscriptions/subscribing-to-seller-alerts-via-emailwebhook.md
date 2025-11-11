---
title: "Subscribing to seller alerts via email/webhook - Help Center - Paddle"
description: "You can subscribe to a wide range of alerts by visiting the alerts/ webhooks page in your Paddle dashboard: http://vendors.paddle.com/alerts-webhooks"
source: "help/sell/set-up-subscriptions/subscribing-to-seller-alerts-via-emailwebhook.html"
---

# Subscribing to seller alerts via email/webhook - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[Sell](/help/sell)[Set up subscriptions](/help/sell/set-up-subscriptions)

Subscribing to seller alerts via email/webhook

Alerts are notifications Paddle sends out after an event occurs. They are also an essential way of integrating subscription services with Paddle. You can subscribe to a wide range of seller alerts by visiting the Developer Tools > Notifications (Paddle Billing) or Events (Paddle Classic) page in your Paddle Dashboard.

You can choose to have alerts sent to you via email, webhook, or both. A full list of alerts can be found [here](https://developer.paddle.com/webhooks/overview) for Paddle Billing, and [here](https://developer.paddle.com/classic/webhook-reference/bd1986c817a40-webhook-reference) for Paddle Classic.

# Paddle Billing

To receive alerts, go to the ‘Notifications’ page and click "New destination" button. You should then be able to select Webhook or Email under the 'Notification type' dropdown menu. You can learn more information about the different alerts by hovering over the tooltip (i) icon. Click "Save destination" once you've configured your preferred settings.

Click [here](https://developer.paddle.com/webhooks/notification-destinations) to learn more about working with notification destinations.

# Paddle Classic

If you choose to subscribe to alerts via email, by default these will be sent to the vendor email address you used during sign-up. You can check what your vendor email address is by selecting ‘Account Settings’ in the menu on the Vendor Settings page in your dashboard, and going to ‘Email’.

Alternatively, you can choose a different email address for receiving email alerts on the ‘Events’ page itself, by using the ‘Email address for receiving email alerts’ field.

If you choose to subscribe to alerts via webhook, you can also do so by entering the URL in the ‘URL for receiving webhooks’ field on the 'Events' page.

You can learn more information about the different alerts by hovering over the tooltip (i) icon.

# Webhook simulator

 _Only applicable to Paddle Classic. To test the webhooks in Paddle Billing, please[sign up for a sandbox account](https://sandbox-login.paddle.com/signup) and test the alerts there instead._

Select the Webhook Simulator button (or [click here](https://vendors.paddle.com/webhook-alert-test)) to access this tool. The Webhook Simulator will allow you to see what data is sent with each alert webhook, and simulate alert webhooks to successfully integrate these with your system.

For example, if you want to test a subscription plan and see which data is sent when a customer signs up so you can enable their access to your product or service, using the Webhook Simulator will allow you to see how you can build your integration to facilitate this.

# Alert History

## Paddle Billing

On the Notifications page, click on the ellipsis button on an active notification destination and click "View logs" to view the historical alerts sent.

For webhook-type notification destinations, you can additionally click the ellipsis button on each event and "View details" for more information.

## Paddle Classic

Select the Alert History button (or [click here](https://vendors.paddle.com/webhook/alerts)) to access this tool. You can check a log of all alerts sent out by Paddle using this. You can also use this to retry any alerts which failed to process if you experienced system issues.