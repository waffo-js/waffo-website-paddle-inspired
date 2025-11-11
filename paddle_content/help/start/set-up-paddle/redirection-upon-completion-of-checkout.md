---
title: "How to redirect upon completion of checkout? - Help Center - Paddle"
description: "This differs between products and subscription plan. Please refer to the full article for more details."
source: "help/start/set-up-paddle/redirection-upon-completion-of-checkout.html"
---

# How to redirect upon completion of checkout? - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[Start](/help/start)[Set up Paddle](/help/start/set-up-paddle)

How to redirect upon completion of checkout?

_This is only applicable to Paddle Classic_

For [products](https://vendors.paddle.com/products), you can define the redirect behavior on the product create/edit page, under the “Set where the users go after checkout” section.

For [subscriptions](https://vendors.paddle.com/subscriptions/plans), the URL needs to be defined in the ‘success’ argument (see Success Redirect property in the [Checkout Parameters](https://developer.paddle.com/reference/5e0171ec215eb-checkout-parameters) documentation), when calling the Paddle.checkout.open() method in your [Paddle.js](https://developer.paddle.com/guides/b4f911a991bd7-overlay-checkout) implementation.

Equally, if using a static link, you can set it in the ‘data-success’ value in your link:

`<a href="#!" class="paddle_button" data-product="12345" data-success="http://your-example-url.com">Buy Now!</a>`