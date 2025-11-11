---
title: "Deprecating TLS 1.0 and 1.1"
description: "TLS 1.0 and 1.1, used by a very small minority of buyers, will be deprecated on the 30th of June 2018: we explain how this may impact you and what you can do."
source: "blog/deprecating-tls-1.0-1.1.html"
---

# Deprecating TLS 1.0 and 1.1

TLS 1.0 and 1.1, used by a very small minority of buyers, will be deprecated on the 30th of June 2018: we explain how this may impact you and what you can do.

![](https://images.prismic.io/paddle/683935ba-533a-4682-906c-88bb428eaf12_mike-wakeling.jpeg?auto=compress%2Cformat&fit=max&w=384)

Author

[Mike Wakeling](/resources/author/mike-wakeling)

Share

[](https://x.com/intent/tweet?text=Deprecating%20TLS%201.0%20and%201.1%20-%20https%3A%2F%2Fwww.paddle.com%2Fblog%2Fdeprecating-tls-1.0-1.1%20via%20%40paddlehq)[](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fdeprecating-tls-1.0-1.1)[](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Fwww.paddle.com%2Fblog%2Fdeprecating-tls-1.0-1.1&title=Deprecating%20TLS%201.0%20and%201.1&source=)

![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbanner-default-light.ae7889e4.jpg&w=3840&q=75)

### Join our newsletter for the latest in SaaS

By subscribing you agree to receive the Paddle newsletter. Unsubscribe at any time.

On the 30th of June 2018 the PCI Security Council, made up of Visa, MasterCard, American Express, Discover and JCB, are deprecating TLS 1.0 and 1.1; this is in an effort to keep card payments secure.

TLS is used to keep web traffic and communications secret. Versions 1.0 and 1.1 have known weaknesses, and continuing to support them would put buyers at risk. To ensure everyone can use the web in a safe and secure manner, the much more secure TLS 1.2 protocol will be required for all payment data after this cut-off date.

To help keep our buyers as secure as possible, Paddle will also be deprecating the use of TLS 1.0 and 1.1 on all our other APIs at this time.

From this date, any buyers using older operating systems or browsers will no longer be supported. Buyers on these older systems will have to upgrade to a newer platform to be able to shop online. This change will be enacted by all online merchants, not just Paddle.

## How does this impact you?

The impact will be minimal for our sellers: after looking at the data, only 0.3% of purchases via Paddle were made using older browsers and operating systems that only support TLS 1.0 and 1.1.

These will cease to work from July 2018 onwards, which means that some of these affected buyers may complain that they can’t use our checkout. The only solution is for them to upgrade to a more recent browser and operating system.

If you are using our APIs with clients that do not support TLS 1.2 you will also need to update them. This typically involves upgrading the operating system or packages on your server.

## What steps can you take?

You can use [How’s My SSL](https://www.howsmyssl.com/s/api.html) to check whether your client supports TLS 1.2.

The How's My SSL service can also be used to check whether your buyers are impacted (although the service charges a subscription in that case), and display a message encouraging them to upgrade rather than opening the checkout. [Contact us](mailto:vendors@paddle.com) if you want to discuss the best way to build a good experience for your buyers.

## What are we doing next?

In order to help you better assess the impact of these changes, before the cut-off date we’ll be temporarily turning off TLS 1.0 and 1.1 over the coming months:

  * For 4 hours on the 29th March
  * For 12 hours on the 19th April
  * For 1 day on the 17th May


We will send you a reminder nearer the time so you can understand the impact of this change, especially around drops in conversion (tracked via Google Analytics for example) and alerts about errors in your applications.

## Which operating systems and browsers will no longer be supported?

To be able to use the checkout buyers will need to use one of the following browsers:

  * Google Chrome: above version 29 (released August 2013)
  * Safari: version 7 and above (which came with MacOS 10.9) (released August 2015)
  * Firefox: above version 26 (released December 2013)
  * IE: version 8 and above BUT buyers will need to have the right service pack for Windows 8 and below (8.1 does support it).


![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fbg-billing-banner.aeafb277.jpg&w=3840&q=75)

## Take the headache out of growing your software business

We manage your payments, tax, subscriptions and more, so you can focus on growing your software and subscription business.

[Get started today](https://login.paddle.com/signup)[Talk to an expert](/demo)