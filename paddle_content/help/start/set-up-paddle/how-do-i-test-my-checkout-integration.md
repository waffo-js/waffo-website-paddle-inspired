---
title: "How do I test my checkout integration? - Help Center - Paddle"
description: "The best way to test your Paddle integration and checkout flow is with our sandbox environment. "
source: "help/start/set-up-paddle/how-do-i-test-my-checkout-integration.html"
---

# How do I test my checkout integration? - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[Start](/help/start)[Set up Paddle](/help/start/set-up-paddle)

How do I test my checkout integration?

You can test your Paddle integration in a few ways. The recommended approach is to use our Sandbox, which keeps test activity completely separate from your live data and reporting.

## **Sandbox**

The best way to test your Paddle integration and checkout flow is with our sandbox environment.

  * If you’re new to Paddle, first[  _sign up for a live account_](https://www.paddle.com/get-started) so we can get your[  _account verified_](https://www.paddle.com/help/start/account-verification). In the meantime, you can[  _sign up for a sandbox account_](https://sandbox-login.paddle.com/signup) and begin testing.

  * If you already use Paddle,[  _sign up for a sandbox account_](https://sandbox-login.paddle.com/signup) to experiment and test safely.


Using Sandbox you can:

  * Use test cards to simulate successful and unsuccessful transactions, including 3D Secure flows

  * Experiment with checkout branding before surfacing it to customers

  * Test end-to-end customer experiences, review automated emails, check access management, and more


For step-by-step guidance and test cards, see our developer docs:[  _Testing with Sandbox_](https://developer.paddle.com/classic/getting-started/c052e9e8d265f-working-with-the-paddle-sandbox#test-cards).

## **Discounts for products**

Prefer running this test in Sandbox. If you perform it live, be aware that it may affect reporting.

Having set up a product (one-time) in your dashboard, you will have a checkout link and the ability to add discounts for your product. Set up a 100% off discount, and apply this during the checkout process to test. For information on customizing emails, see[  _Editing the styling of invoices/emails_](https://www.paddle.com/help/start/set-up-paddle/editing-the-styling-of-invoicesemails).

## **Test plans for recurring billing**

When setting up recurring billing with Paddle, create test plans in Sandbox (for example, with a free price) and verify that your integration handles the same[  _webhook events_](https://developer.paddle.com/webhooks/overview) as paid plans, such as payments, plan changes, and cancellations. Once you’re satisfied in Sandbox, you can proceed to live usage.