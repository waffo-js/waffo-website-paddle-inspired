---
title: "Contact/Company properties for HubSpot - Help Center - Paddle"
description: "Here is a breakdown of the data you can pull from ProfitWell into your HubSpot properties for contacts or companies       Customer ID    This customer ID is t"
source: "help/profitwell-metrics/export-data/hubspot/hub-spot-api-fields.html"
---

# Contact/Company properties for HubSpot - Help Center - Paddle

Live webinar

Find out what’s working and what’s not for app growth, and how to use external payments to capture intent and drive growth in Q5

[Register now](https://www.paddle.com/events/webinars/why-q5-is-the-underrated-opportunity-in-mobile-app-growth?utm_medium=website&utm_source=website-banner&utm_campaign=webinars_fy2025_q4_core_revenuecat_webinar_18nov&utm_content=homepage-banner)

[Help](/help)[ProfitWell Metrics](/help/profitwell-metrics)[Export Data](/help/profitwell-metrics/export-data)[HubSpot](/help/profitwell-metrics/export-data/hubspot)

Contact/Company properties for HubSpot

Here is a breakdown of the data you can pull from ProfitWell into your HubSpot properties for contacts or companies.

  * **Customer ID****:** This customer ID is the one you see in your ProfitWell customer profiles; it reflects the unique ID assigned to a specific customer within your billing system (Stripe, Braintree, Chargebee, etc).
  * **First Name****:** First name of the customer will be synced with HubSpot through ProfitWell if it exists within the integrated billing system; if not, it will then left as empty if unknown.
  * **Last Name****:** Last name of the customer will be synced with HubSpot through ProfitWell if it exists within the integrated billing system; if not, it will then left as empty if unknown.
  * **MRR****:** Monthly recurring revenue (MRR) of each existing customer will be synced from ProfitWell into HubSpot, in the designated display currency. Within HubSpot, it will be an unformatted number unless you "edit property" and change it to "Currency" format.


  


![](https://files.helpdocs.io/gvtU4sx5eD/articles/edd4c5x17t/1590591428025/screen-shot-2020-05-27-at-04-56-53.png)

  


  * **P****lans:** Subscription plans of all customers will be synced with HubSpot from ProfitWell, through the live data feed pulled directly from the integrated billing system.
  * **S****tatus:** Subscription plan status of all customers will be synced with HubSpot from ProfitWell in one of the following forms: active, trialing, cancelled, churned_trial, churned_voluntary, churned_delinquent.
  * **Created On****:** The date a user was originally created will be populated within HubSpot directly from ProfitWell; it may not necessarily represent the first instance of a paying transaction (e.g. individuals on trials also count as users.
  * **A****ctivated On:** The date a user becomes an actively paying customer is synced with HubSpot from ProfitWell once a transaction occurs, as reflected through the billing system.
  * **C****hurned On:** The date of a customer's most recent churn is synced with HubSpot from ProfitWell; it represents the end of the final billing cycle after a customer cancels.
  * **Engagement** : The quartile of customer activity, based on the total number of logins within 30 days.
  * Total Spend: The total revenue a customer has paid you in his/her lifetime (includes recurring revenue, along with one-time payments, etc.- essentially cash flow)


  


Note:

**E****mail** **is pulled directly into your HubSpot account:** When an email is updated within ProfitWell, it will sync with HubSpot and connect with the associated customer; this data may possibly be null, non-unique, or incorrect depending on the fields filled out by the customer, so it shouldn't be used as the unique identifier. If you aren't seeing ProfitWell data loading for a certain customer, then it is likely that the email is not connected to any HubSpot contact.

**If ProfitWell Metrics doesn't find an existing customer under the same email in HubSpot, then it will add a new customer to HubSpot.** ProfitWell Metrics will alter your existing and new records in HubSpot.

To set up the integration, check out our [HubSpot connection instructions here](https://learn.profitwell.com/article/dx0nf76agj-setting-up-the-hub-spot-integration).