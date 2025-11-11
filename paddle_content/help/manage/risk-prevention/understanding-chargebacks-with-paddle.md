---
title: "Understanding Chargebacks with Paddle - Help Center - Paddle"
description: "Paddle receives 2 types of events in regards to chargebacks  Chargebacks  and  Pre Chargeback  Alerts This document will explain each type of event."
source: "help/manage/risk-prevention/understanding-chargebacks-with-paddle.html"
---

# Understanding Chargebacks with Paddle - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[Manage](/help/manage)[Risk Prevention](/help/manage/risk-prevention)

Understanding Chargebacks with Paddle

  


### **What is a Chargeback?**

A chargeback happens when a buyer disputes a payment with their bank or card provider. As Paddle is the Merchant of Record (MoR) for all transactions processed through our platform, the dispute is raised against Paddle rather than you, the seller.

When a chargeback occurs, the funds are withdrawn from Paddle (not the seller), and a chargeback fee is applied by the payment provider. We then deduct both the transaction amount and the fee from your supplier account balance. 

There are two main types of chargeback scenarios in Paddle Billing:

  * **Chargeback** : The buyer disputes the charge directly.  
  


  * **Pre-Chargeback Alerts**~~:~~ We receive a pre-chargeback alert from our fraud tooling partners, and proactively refund the payment to avoid the chargeback being filed.  
  


Each type follows a different process, which we’ve outlined below.

Chargebacks are a common part of online payments, especially in software transactions. Resolving issues early can help avoid chargebacks; for example, offering refunds to dissatisfied buyers may prevent disputes.

  


* * *

  


### **Chargeback Rates**

Keeping your chargeback rate low is critical for maintaining a good standing with Paddle and card payment networks. Paddle calculates chargeback rates by comparing the total dollar value of chargebacks received against your total transaction volume for a given month. This method provides a clearer understanding of their impact on your account.

  * **Acceptable Chargeback Rate:** Below **0.65%** of transaction volume.


If your chargeback rate exceeds 0.65%, Paddle may require changes to your processes to bring the rate down. This will always be done collaboratively with our Risk Team, and any changes to your account will be communicated in advance.

To reduce chargeback rates, consult the **Best Practices** section in our [Seller Handbook](https://www.paddle.com/seller-guides/seller-handbook) and [our blog post](https://www.paddle.com/resources/chargebacks) on chargebacks.

  


* * *

  


### **Standard Chargeback Process**

#### **How it works:**

  1. The buyer disputes a charge with their bank.

  2. The bank issues a chargeback and withdraws the funds.

  3. Our PSP notifies us and applies a chargeback fee.

  4. Paddle deducts both the transaction amount and the fee from your seller balance.

  5. Paddle’s Dispute Defense System automatically contests chargebacks by gathering evidence. This evidence may include communication with the buyer, subscription payment history, and proof of authorization for the purchase.  
The system is fully automated, and additional evidence submitted by sellers is not required or accepted.

  6. The bank reviews the case and decides the outcome:

     * If the bank **sides with the buyer** : no further action is taken.

     * If the bank **sides with Paddle** : we return the funds and chargeback fee to your seller balance.  
  


  7. If the buyer raises a **second dispute (pre-arbitration)** , we do not contest it and treat it like a standard chargeback.


_N.B Even if a dispute is won, it still counts towards your chargeback rate._

#### **What you'll see in the Paddle Dashboard:**

  * The transaction will appear as fully refunded.

  * Your earnings from the sale are adjusted to £0/$0/€0.

  * A chargeback fee is applied, visible under the "Earnings" section of the transaction. For card payments, the fee is $15/£15/€15, for PayPal transactions it is $20/£20/€20.


You'll see a clear indication that the payment was disputed.

  


* * *

  


### **Chargeback Reversal**

If Paddle wins the dispute, we’ll return the full transaction amount and chargeback fee to your seller balance—even if the fee isn’t refunded to us.

  


* * *

  


### **Pre-Chargeback Alerts**

Sometimes, before a chargeback is finalised, we receive an alert from our fraud partners that a chargeback is likely to take place. These alerts give us a short window (typically 48 hours) to take action. They allow for proactive resolution and help maintain an acceptable chargeback rate.

#### **How it works:**

  1. The buyer disputes the charge with their bank.

  2. Paddle receives a Pre-Chargeback Alert.

  3. We issue a full refund to the buyer **_before_** the chargeback is finalised.

  4. This prevents the chargeback from being filed.

  5. A chargeback fee is still applied to cover the cost of the alert.


On rare occasions, the chargeback may still go through even after a refund. In those cases, we handle it as a standard chargeback.  
  


### **What you'll see in the Paddle Dashboard:**

  * The transaction will be listed as refunded and adjusted to £0/$0/€0.

  * You'll see an entry for the chargeback fee $15/£15/€15 (deducted from your balance) in the earnings breakdown.


The refund will be visible under the transaction details.

  


* * *

  


### **How to Identify Pre-Chargeback Alerts and Disputed Charges**

Paddle proactively manages disputes to minimize their impact on your account. Here’s how we handle them:

  * **Pre-Chargeback Alerts** : If an early-stage dispute is detected, a "chargeback_warning" adjustment is created. The disputed amount is refunded, and a service fee is applied, preventing the dispute from affecting your chargeback rate.

  * **Standard Chargebacks** : If no early warning is received, a "chargeback" adjustment is created when the dispute occurs. This can impact your chargeback rate.

  * **Reversed Chargebacks** : If Paddle successfully disputes a chargeback, a "chargeback_reverse" adjustment restores the refunded amount and reverts the associated fees.


For detailed information on chargeback adjustments, refer to the [Developer Documentation](https://developer.paddle.com/build/transactions/create-transaction-adjustments#background-chargebacks).

In Paddle Classic (PC), you may also see an “internal chargeback” note on the order page, providing additional details about the chargeback’s status.

  


* * *

  


### **How We’ll Notify You About Chargebacks and Alerts**

You can identify chargebacks and Pre-Chargeback Alerts in the Vendor Dashboard:

  * **Paddle Classic** : Transactions with chargebacks or Pre-Chargeback Alerts include a note indicating the event.

  * **Paddle Billing** : Labels specify whether the transaction is a Pre-Chargeback Alert or a standard chargeback.


For instructions on enabling notifications for disputes, visit our [Help Article](https://www.paddle.com/help/manage/risk-prevention/how-do-i-get-notified-about-disputes) on notifications.