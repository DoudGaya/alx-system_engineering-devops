# Incident Report: Cloud Storage Outage (March 20, 2023)


## Issue Summary:
On March 20, 2023, starting at 3:00 AM GMT+1, our cloud storage service experienced an outage that lasted for 6 hours until 9:00 AM GMT+1. During this time, users were unable to access their files and experienced slow upload and download speeds. Approximately 80% of our users were affected by this outage.

## Timeline:
-  3:00 AM GMT+1: The issue was detected by our monitoring system which alerted the on-call engineer.
- 3:05 AM GMT+1: The engineer confirmed the issue and started investigating.
- 3:10 AM GMT+1: The engineer noticed that the network connectivity between our cloud storage servers and the database servers was intermittent.
- 3:15 AM GMT+1: The engineer initiated a failover to the backup database servers, but this did not resolve the issue.
- 3:30 AM GMT+1: The engineer noticed a high number of network connections from a single IP address, which suggested a possible DDoS attack.
- 3:45 AM GMT+1: The engineer escalated the incident to the security team for further investigation.
- 4:00 AM GMT+1: The security team confirmed that it was a DDoS attack and started working on mitigating the attack.
- 9:00 AM GMT+1: The DDoS attack was mitigated, and the cloud storage service was restored to full functionality.



## Root cause and resolution:
The root cause of the outage was a DDoS attack targeting our cloud storage service. The attack caused a high number of network connections, which overwhelmed our network infrastructure and caused intermittent connectivity between the cloud storage servers and the database servers.
To resolve the issue, the security team implemented several measures to mitigate the DDoS attack, including rate-limiting network connections from the attacking IP address and deploying additional network infrastructure to handle the increased traffic. Additionally, we updated our DDoS mitigation plan to include more proactive measures to prevent and mitigate DDoS attacks in the future.


## Corrective and preventative measures:
To prevent similar incidents from occurring in the future, we have identified the following areas for improvement:
- Implement additional network monitoring to detect and mitigate DDoS attacks more quickly.
- Update our DDoS mitigation plan to include more proactive measures, such as using a content delivery network (CDN) to absorb DDoS attacks before they reach our infrastructure.
- Increase redundancy in our network infrastructure to handle increased traffic during DDoS attacks.
- Conduct regular DDoS attack simulations to test our response plan and identify areas for improvement.
To address these issues, we have identified the following tasks:
- Implement additional network monitoring using a network intrusion detection system (NIDS).
- Evaluate and select a CDN provider to use as a proactive DDoS mitigation measure.
Implement additional network infrastructure to increase redundancy and handle increased traffic during DDoS attacks.
- Schedule regular DDoS attack simulations to test our response plan and identify areas for improvement.
 
 ## Conclusion

 This incident report documents the timeline of events, root cause analysis, and corrective and preventative measures for the cloud storage outage on March 20, 2023. We will continue to monitor and improve our infrastructure to provide reliable

