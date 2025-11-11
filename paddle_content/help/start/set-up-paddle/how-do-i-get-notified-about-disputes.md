---
title: "How do I get notified about disputes? - Help Center - Paddle"
description: "You can set up chargeback alerts via email webhook or both methods through your vendor dashboard  Paddle Classic   Go to Developers Tools on the vendor d"
source: "help/start/set-up-paddle/how-do-i-get-notified-about-disputes.html"
---

# How do I get notified about disputes? - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[Start](/help/start)[Set up Paddle](/help/start/set-up-paddle)

How do I get notified about disputes?

You can set up alerts for disputes via email, webhook, or both methods through your vendor dashboard.

## Paddle Classic

  * Under “Developer Tools” click on "Events".
  * Find the “Risk & disputes” category.
  * Tick the preferred notification method (email or webhook).


[You can find more details about the risk and dispute alerts here](https://developer.paddle.com/classic/webhook-reference/ZG9jOjI1MzU0MDA0-risk-and-dispute-alerts).

##   


## Paddle Billing

  * Under “Developer Tools” click on “Notifications”.
  * Select “+ New destination”. 
  * Choose webhook or email as the notification type. 
  * Subscribe to “Adjustment” events.


Please note that refunds and chargebacks are categorized [under adjustments in Paddle Billing](https://developer.paddle.com/api-reference/adjustments/overview#adjustments).

For more details on working with notification destinations in Paddle Billing, [head to our developer docs here](https://developer.paddle.com/webhooks/notification-destinations).