---
title: "Retain Cancellation Flows Configuration - Help Center - Paddle"
description: "Overview  Retains Cancellation Flows can help you save more customers via dynamic salvage attempts as well as provide robust cancellation insights Well gath"
source: "help/profitwell-metrics/retain/how-it-works/cancellation-flows-configuration.html"
---

# Retain Cancellation Flows Configuration - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[ProfitWell Metrics](/help/profitwell-metrics)[Retain](/help/profitwell-metrics/retain)[How it Works](/help/profitwell-metrics/retain/how-it-works)

Retain Cancellation Flows Configuration

### Overview

Retain's Cancellation Flows can help you save more customers via dynamic salvage attempts, as well as provide robust cancellation insights. We’ll gather insights around why they’re cancelling, as well as what they found valuable about your service, to ensure everyone gets a custom curated off-boarding and salvage experience.

### Setup

  1. [**Click here**](https://learn.profitwell.com/article/nrk5v7jn1u-how-to-install-the-cancellation-flow-snippets) to see instructions on how to install this in your web app.
  2. [**Download this template here**](https://assets.paddle.com/assets/retain/paddle-retain-cancel-flow-setup-form.xlsx) to configure your survey/salvage attempt/salvage offer preferences.


### How does it work?

When customers click on the "cancel" button in your web-app, we start by asking them to provide a cancellation reason and a satisfaction insight:

![](https://files.helpdocs.io/gvtU4sx5eD/articles/abe1c70qxh/1644444960635/screen-shot-2022-02-09-at-5-15-28-pm.png)

Not only are we asking your customers why they’re leaving, but we’re also asking them what they liked about your product/service. **By honing in on the psychological phenomenon of the nostalgia effect, we are teeing up each customer to be more willing to stick around and accept a salvage attempt** \- "Since you liked our support so much, how about a 1:1 account review to make sure you're getting the most value out of our platform?"

Plus, you'll get more dynamic insights that will help you better determine which salvage attempts are more effective than others for your customers.

#### Salvage attempts

Based on your customers' responses to the survey, we can curate their experience by directing them to one of three salvage attempts:

  1. **Pause subscription**
     1. This is especially effective if your business is more seasonal - where while your customers may not be getting value right now, they plan on coming back in a few months.
  2. **Switch plan**
     1. This is especially effective if you have a lower cost plan that customers can switchover to and still get some value at a more affordable price. This is also a great option if you have a maintenance plan where customers don't have feature access but can save their data/preferences with you at a low cost.
  3. **Contact support**
     1. This is especially effective if customers express that they like your support but don't seem to be getting value/don't know how to fully leverage your features. We want to help set your support team for success, and so we'll also provide them with all the context they need (i.e., survey responses) before they talk to your customers.
     2. There are **two ways** your customers can contact support - we can let customers book meetings with your support team via Calendly, or we can email your support team/create a ticket whenever a customer wants to chat.


#### Salvage offer

![](https://files.helpdocs.io/gvtU4sx5eD/articles/abe1c70qxh/1644449306410/screen-shot-2022-02-09-at-6-28-17-pm.png)

If your customers do not accept the initial salvage attempt they were given, you can offer a final discount salvage offer.

**  
**

**Cancellation Flow Best Practices**

  1. There currently is **no** testing environment for Cancellation Flows, so sellers will have to “test” in production.
  2. Cancel Flows are**only triggered for paying customers, and not trialling/free customers** , even if the trialers have an upcoming payment. If such a customer tries to cancel, they will only get a “Click to Confirm Cancellation” button.
  3. There isn't a way to trigger cancel flows for newly-created customers, because they haven't been ingested into our database yet before the cancellation triggers.**A period of 3-6 hrs is needed for the customer to be ingested into the database.**
  4. The salvage offer provided (discount, pause, etc) is based on the survey’s satisfaction insight (what you liked), and not the cancellation insight (what you didn’t like).
  5. Plan switches and discounts happen **immediately** , not at the next billing cycle.