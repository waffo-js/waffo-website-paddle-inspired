---
title: "Are my trial subscriptions compliant? - Help Center - Paddle"
description: "Over the course of an introductory trial or promotion, the subscriber must repeatedly be provided with the following points in order for your trial subscript..."
source: "help/start/intro-to-paddle/are-my-trial-subscriptions-compliant.html"
---

# Are my trial subscriptions compliant? - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[Start](/help/start)[Intro to Paddle](/help/start/intro-to-paddle)

Are my trial subscriptions compliant?

Throughout an introductory trial or promotion, the subscriber must repeatedly be provided with the following points for your trial subscriptions to remain compliant:

  * The fact the customer has signed up for a subscription
  * The date the subscription started
  * The duration of the trial period
  * The subscription name
  * The recurring price and next payment date
  * A link to somewhere they can update their payment method, or cancel their subscription


This is shared across the following emails and transaction receipts:

  * Welcome Notification Email: The initial email they receive when signing up, confirming that they’ve joined on a free trial or discounted period
  * Welcome Notification Receipt: Linked from the welcome email is the receipt confirming the amount paid, even if zero (example image shown below)
  * Enhanced Notification Email: A mandatory one-off email that tells them their discounted period is ending and they are about to be charged for the first time.
  * Initial Transaction Email: An email that is sent to them after they make the first payment on their subscription after their initial trial/discounted period has ended.
  * Initial Transaction Receipt: Linked from that email is the receipt confirming payment.


![Initial Subscription Receipt](https://cdn.kustomerhostedcontent.com/media/5b64d5e964987defc0b2a2de/1bb9a67e2fa4d53b622b5dfc619f92e8.png)

Other subscription emails such as the optional pre-billing notifications and recurring subscription receipts are unaffected by these compliance changes.

## Which subscriptions does this apply to?

The more detailed receipts and emails discussed on this page only relate to any subscription which:

  * has an initial ‘trial’ period at a reduced price, e.g. free for a month
  * or has a non-recurring coupon applied to a subscription for an initial period, e.g. first 2 months of subscription is 10% off


All other ‘regular’ subscriptions are exempt and will not show this additional information on emails & receipts, nor will we send non-trial subscriptions the additional emails, such as the enhanced notification or the initial transaction email.

### I offer a subscription that does not have a free or promotional trial. Does this apply to me?

No, this would not apply to you.

## Do I have to do anything for my trial subscriptions to remain compliant?

**No.**

Paddle manages your subscription receipts and email flows so you don’t need to change anything; as your Merchant of Record, we handle the necessary compliance and development work for you.

The only exception is if you are providing a trial/promo period on a subscription by using our Charges API. See below for more details on what you need to do in that situation.

## What does this mean if I’m using the Charges API to manage subscriptions with an initial trial/promo period?

If you are using the [Charge API](https://developer.paddle.com/api-reference/23cf86225523f-create-one-off-charge) to manage a promotional or trial subscription yourself, then you will need to send the following required emails yourself. This is because we won’t be able to determine, for example, when the trial period will expire to supply the customer with the enhanced notification. You need to send the:

  * Welcome Notification Email ([example here](https://www.paddle.com/help/manage/your-customers/which-emails-will-customers-receive#welcome-notifications)): An initial subscription confirmation email, confirming that they’ve joined on a free trial or discounted period. As with our version, this should include confirmation of:
  * The fact the customer has signed up for a subscription
  * The date the subscription started
  * The duration of the trial period
  * The subscription name
  * The recurring price and next payment date
  * A link to somewhere they can update their payment method, or cancel their subscription. This can come from our `update_url` and `cancel_url` links returned from the [List Users API](https://developer.paddle.com/api-reference/e33e0a714a05d-list-users).
  * An ‘Enhanced Notification Email’ ([example here](https://www.paddle.com/help/manage/your-customers/which-emails-will-customers-receive#enhanced-notifications)): Your version of our enhanced notification should tell them their discounted period is ending and that they are about to be charged for the first time.
  * This needs to be sent 7+ days before you charge the customer for their first regular subscription payment (or to notify them if the price or billing period has changed)
  * It should also provide a link for them to update their payment method or cancel their subscription.


Also, we are going to add an optional field to the Charges API which you should include when you want to charge the customer their initial full payment (post-trial/discount). We’ll then still be able to send on your behalf the final requirement of the:

  * Initial Transaction Email: An email is sent to them after they make the first payment on their subscription after their initial trial/discounted period has ended.
  * Initial Transaction Receipt: Linked from that email is the receipt confirming payment.


VISA will conduct spot checks and may ask us to block Sellers who are not using the Charges API in a compliant manner, so implementing these flows are important.

## Could these emails negatively affect churn?

These emails may prompt customers who did not want to pay a recurring fee to contact you regarding the cancellation.

However, for the majority of customers, the increased transparency with subscription details leads to a better customer experience and improved brand perception.

## When will these changes be live?

All these changes are live as of July 2020.