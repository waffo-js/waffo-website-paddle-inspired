---
title: "Which emails will customers receive on Paddle Classic? - Help Center - Paddle"
description: "By default, Paddle will email customers with their order receipts along with any instructions you have provided for products. The best way to preview the ema..."
source: "help/manage/your-customers/which-emails-will-customers-receive.html"
---

# Which emails will customers receive on Paddle Classic? - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[Manage](/help/manage)[Your customers](/help/manage/your-customers)

Which emails will customers receive on Paddle Classic?

By default, Paddle will email customers with their order receipts along with any instructions you have provided for products. The best way to preview the emails your customers will receive is to [test your checkout integration](https://www.paddle.com/help/start/set-up-paddle/how-do-i-test-my-checkout-integration) using the full purchase & refund method.

Customers may also receive emails for the following:

  * [Order Receipts](#order-receipts)
  * [Fulfillment](#fulfillment)
  * [Fulfillment Failures](#fulfillment-failures)
  * [Refunds](#refunds)
  * [Checkout Recovery](#checkout-recovery)
  * [Welcome Notifications (Subscriptions)*](#welcome-notifications)
  * [Initial Transaction (Subscriptions)*](#initial-transaction)
  * [Pre-Billing Notifications (Subscriptions)*](#prebilling-notifications)
  * [Enhanced Notifications (Subscriptions)*](#enhanced-notifications)
  * [Failed Billing Notifications (Subscriptions)*](#failed-billing-notifications)
  * [Paused Billing Notifications (Subscriptions)*](#paused-billing-notifications)
  * [Cancelation Notifications (Subscriptions)*](#cancelation-notifications)


* Note: Please do not use the word ‘Subscription’ in your subscription plan name to avoid this word being duplicated in the subscription emails, as this will automatically be added to the email.

We have also localized all these transactional emails. See the [Email Localization](#email-localization) section for more details.

## Order Receipts

We send a confirmation email to customers when they make a purchase.

**Subject Line:** _Your Company Name receipt_

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/276ed48d8bfbfe0f1670174474731847.png)

## Fulfillment

Once the payment is processed, customers receive the following email detailing how they can activate and start using your product.

**Subject Line:** _Your Product Name order_

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/8785c798308075b45834f90fa5856e52.png)

## Fulfillment Failures

If there is a problem delivering a product or plan via [webhook fulfillment](https://developer.paddle.com/webhook-reference/da25d9740f4c7-fulfillment-webhook)*, customers will receive the following notification.

**Subject Line:** _Unable to process your order for Product Name_

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/e3aee7cea09a82ac8699f51a2c8eae25.png)

* Fulfillment can also be referred to as ‘lockers’ in the API developer documentation.

## Refunds

You’re able to issue a [full or partial refund](https://www.paddle.com/help/manage/your-customers/can-i-issue-refunds-and-are-they-free) from the order page on the [Transactions page of your Paddle dashboard](https://vendors.paddle.com/orders). Upon issuing a refund, customers will receive the following email notification.

**Subject Line:** _Confirmation of partial/full/VAT refund for Product Name_

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/e1e3858592940e9ef6f08b4738226888.png)

## Checkout Recovery

Using Paddle you’re able to switch on [checkout recovery](https://www.paddle.com/help/start/set-up-paddle/what-is-checkout-recovery) \- a feature whereby we attempt to recover any incomplete checkouts for your products. You’re able to switch checkout recovery on/off on the [Recover Settings page of your Paddle dashboard](https://vendors.paddle.com/recover-settings).

If checkout recovery is switched on, customers will receive two email notifications. The first one is sent after 90 minutes+ of checkout inactivity:

**Subject Line:** _Finish your Product Name Purchase_

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/854b96a1609a36d635fe5ffab5a63c6c.png)

A second and final email is sent out 7 hours+ following the first email if they have not completed their purchase since the previous email.

## Welcome Notifications

When a user joins a subscription containing a one-off coupon or a trial period they receive an email confirming its start with info about the trial, such as when it ends. Read our guide on [trial subscriptions](https://www.paddle.com/help/start/intro-to-paddle/are-my-trial-subscriptions-compliant) for more details.

**Subject Line:** _Welcome to Product Name_

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/974521e1225d9b95ce38abc6aca88959.png)

## Initial Transaction

When a subscriber has been on a trial subscription and that trial period ends, we then send an email to confirm they have made their first regular payment. Read our guide on [trial subscriptions](https://www.paddle.com/help/start/intro-to-paddle/are-my-trial-subscriptions-compliant) for more details.

**Subject Line:** _Your Company Name receipt_

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/c27a48aeefd3d92bdb03637ec36a8ba6.png)

## Pre-Billing Notifications

You’re able to switch on pre-billing notifications for subscriptions and specify the number of days before the next billing date in which they are delivered in the [Recover Settings page of your Paddle dashboard](https://vendors.paddle.com/recover-settings). For each pre-billing reminder, customers will be sent the following email notification:

**Subject Line:** _Your Product Name Subscription will renew soon_

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/ede767861612808926f629467c0fc3a5.png)

## Enhanced Notifications

When a customer is in the middle of a trial subscription (a free or discounted initial period) then we’ll send a message before their trial period expires to let them know they’re about to start paying. Read our guide on [trial subscriptions](https://www.paddle.com/help/start/intro-to-paddle/are-my-trial-subscriptions-compliant) for more details.

**Subject Line:** _We hope you’re enjoying your Product Name subscription_

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/8df55d9b7e8f9bb205a4693b1e6e7eb5.png)

## Failed Billing Notifications

You’re able to switch on failed billing notifications for subscriptions (recommended) and specify how often we should retry the payment in the [Recover Settings page of your Paddle dashboard](https://vendors.paddle.com/recover-settings). For each failed billing attempt, customers will receive the following notification:

**Subject Line:** _Your Product Name subscription payment failed_

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/725052af8ceec834cec359959ca616da.png)

## Paused Billing Notifications

As an alternative to canceling a subscription when all payment attempts have failed, you can choose to pause the subscription instead. This will give your customer a chance to resolve their payment issue in their own time and restart their subscription again.

**Subject Line:** _We’re sad to see you go_

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/5375189a910bc11298acb063f776bb2d.png)

## Cancelation Notifications

When a buyer’s subscription is canceled they will receive an email that confirms the cancelation. As usual, any responses from this email go to our dedicated Buyer Support team.

**Subject Line:** _Your Subscription for Company Name has been canceled._

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/0093f3cb9bd9d26f53ea17290751236d.png)

## Email Localization

Paddle automatically translates these emails into the 16 languages currently supported in the Checkout: English, French, Portuguese, German, Spanish, Russian, Japanese, Italian, Polish, Dutch, Arabic, Chinese (simplified), Korean, Swedish, Danish, and Norwegian. This means customers will receive all transactional emails in the language they checkout in, which can help decrease involuntary churn and boost conversions in the post-purchase journey*. Here is an example of a Cancelation Notification in Danish:

![](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/24edf65bd1a584d14030531d40961940.png)

* Note: If you don’t want to offer localized transactional emails to customers, please [contact](mailto:sellers@paddle.com) our Customer Support team who will be able to disable this feature for you.