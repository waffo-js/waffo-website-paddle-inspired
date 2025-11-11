---
title: "Customer data for Intercom - Help Center - Paddle"
description: "Here is a breakdown of data pushed from ProfitWell into Intercom for associated Customer and Company if available    Customer ID  This unique ID matches th"
source: "help/profitwell-metrics/export-data/intercom/customer-details-for-intercom.html"
---

# Customer data for Intercom - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[ProfitWell Metrics](/help/profitwell-metrics)[Export Data](/help/profitwell-metrics/export-data)[Intercom](/help/profitwell-metrics/export-data/intercom)

Customer data for Intercom

Here is a breakdown of data pushed from ProfitWell Metrics into Intercom (for associated Customer and Company, if available).

  * **Customer ID:** This unique ID matches the ID from your subscription management solution, or the one you assigned yourself.
  * **First Name:** First name will be pulled by ProfitWell if the data exists.
  * **Last Name:** Last name will be pulled by ProfitWell if the data exists.
  * **MRR:** Monthly recurring revenue (MRR) of each existing customer will be synced from ProfitWell into Intercom, in the designated display currency. (note: within Intercom, it will be an unformatted number unless you "edit property" and change it to "Currency" format).
  * **Plans:** Subscription plans of all customers will be synced with Intercom from ProfitWell through the live data feed.
  * **Status:** Subscription plan status of all customers will be displayed in one of the following forms: active, trialing, cancelled, churned_trial, churned_voluntary, churned_delinquent.
  * **Created On:** The date a user was originally created; it may not necessarily represent the first instance of a paying transaction (e.g. individuals on trials also count as users).
  * **Activated On:** The date a user becomes an actively paying customer, as reflected through the billing system.
  * **Churned On:** The date of a customer's most recent churn; it represents the end of the final billing cycle after a customer cancels.
  * **Engagement** : The quartile of customer activity, based on the total number of logins within the last 30 days.
  * **Total Spend:** The total revenue a customer has paid you in his/her lifetime (includes recurring revenue, along with one-time payments, etc.- essentially cash flow)


Notes:

**This integration maps customer data properties to both the customer and company level** , if known. If customer email within ProfitWell Metrics matches the customer email within Intercom, then the available data will be successfully matched and pushed through to customer and company details.

  


**E****mail** **is pulled directly into your Intercom account:** When an email is updated within ProfitWell, it will sync with Intercom and connect with the associated customer; this data may possibly be null, non-unique, or incorrect depending on the fields filled out. If you aren't seeing ProfitWell Metrics data loading for a certain customer, then it is likely that the email is not connected to any Intercom contact.

  


**If ProfitWell Metrics doesn't find an existing customer under the same email in Intercom, then it will add a new customer to Intercom.** ProfitWell Metrics will alter your existing and new records in Intercom. Please note that if you are on a paid tier based on People Reached, this integration sync could potentially increase the total number of customers stored inside of Intercom that you may be reaching.