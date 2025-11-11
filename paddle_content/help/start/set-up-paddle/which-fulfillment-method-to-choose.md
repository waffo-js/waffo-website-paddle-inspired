---
title: "Which fulfillment method to choose? - Help Center - Paddle"
description: "There are four ways to deliver your product to customers:   Server Notification (Webhook)  This is what the majority of our sellers use. Webhooks are HTTP GE..."
source: "help/start/set-up-paddle/which-fulfillment-method-to-choose.html"
---

# Which fulfillment method to choose? - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[Start](/help/start)[Set up Paddle](/help/start/set-up-paddle)

Which fulfillment method to choose?

_This is only applicable to Paddle Classic_

There are four ways to deliver your product to customers:

**Server Notification (Webhook)**  
This is what the majority of our sellers use. Webhooks are HTTP GET/POST requests sent to your server, used to receive data from Paddle and for your server to communicate back. This is typically used to send order-specific data to a customer after the payment process (e.g. a unique license code). It is our most flexible fulfillment method, which allows you to build your own user database from the data you receive. For more information regarding this, [click here](https://developer.paddle.com/webhook-reference/ZG9jOjI1MzUzOTkx-order-fulfillment).

**Download**  
An email with download instructions will be sent directly to the customer with a link to the file uploaded* or the download URL specified.

* Please note that any files uploaded and hosted by Paddle will not be order-authenticated (and will provide a static download link for all buyers). If you’re selling a product that does not require any order verification to use it (such as e-books and graphic files), we would strongly recommend that you consider hosting these files using an alternative provider.

**License List**  
Upload a plain text document (`.txt`) file containing a list of licenses (newline-separated). When a customer purchases the product, they will be emailed a license key and any information/instructions that you have specified. Once this list has been exhausted, it will throw an error and you will be contacted by someone at Paddle requesting more license codes be added.

**Paddle License (SDK)**  
Generate licenses specifically for use with your Mac application using our licensing feature within the Paddle SDK. For more information on how to build this integration, [click here](https://developer.paddle.com/reference/ZG9jOjI1MzU0MDY0-license-activation-mac).