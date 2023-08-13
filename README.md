# CloakR

# Pitch:

# Devfolio:

- Name:

```jsx
CloackR;
```

- Tagline:
- Problem it solves

```markdown
CloakR emerges as a transformative solution addressing critical challenges in contemporary crime reporting and community safety. In today's society, crime lurks around every corner, posing threats to individuals and neighborhoods. However, the act of reporting crimes often faces significant barriers, including fear of retaliation, concerns about personal privacy, and the absence of effective, anonymous channels. These obstacles lead to underreporting, hinder law enforcement efforts, and create an environment where criminal activities can persist unchecked.

The existing crime reporting systems also lack a sense of active participation and engagement from the community. Individuals are left feeling disconnected from law enforcement efforts and unsure of how they can contribute to the safety of their neighborhoods. Moreover, the spread of misinformation, whether intentional or unintentional, further exacerbates the challenges faced by law enforcement agencies and can hinder investigations.

CloakR's AI-powered 'Listeners' continuously monitor news outlets, extracting relevant crime-related information. This data, combined with official police submissions, forms a comprehensive crime database that's updated in real-time. This central database of crimes will power an app, allowing users to easily and confidentially view, report, and share tips about any crime they may have information or evidence on.

But here's the exciting part – every valuable tip counts. When a tip leads to a successful investigation, the anonymous user behind it gets rewarded. These rewards, sponsored by the government, incentivize active participation and create a sense of ownership in community safety.

CloakR takes data security seriously. User Aadhar information is encrypted and stored in the blockchain, ensuring privacy and transparency. In rare cases of misinformation, our smart contract system enables accountability, discouraging any attempts to hinder police investigations.
```

- Challenges:

```markdown
During the development of our platform, we encountered several challenges that led to innovative solutions. To address the issue of spam accounts and the potential submission of misleading or false information detrimental to police investigations, we devised a comprehensive approach. Each user is required to link their Aadhar, which is then securely encrypted and stored within the blockchain, beyond our access. In rare instances, such as when false information is deliberately submitted to obstruct ongoing investigations, a smart contract will facilitate the decryption of Aadhar details from the blockchain. This measure enables the police to access the individual's information for legal actions and consequences. Additionally, we established an admin panel for meticulous moderation and filtering of information before it is relayed to the police dashboard.

Furthermore, ensuring the platform's efficacy demanded a substantial, real-time database to accommodate contributions from users nationwide, even though collaboration with police from all regions might not be uniform. To tackle this challenge, we introduced the concept of a Listener, a perpetually active component that continuously monitors online news outlets. Employing advanced web-scraping techniques and a cutting-edge NLP model, the Listener extracts pertinent crime-related details from these sources. This innovative solution ensures a robust and up-to-date database, empowering users across the country to actively engage and earn incentives while aiding the cause of crime prevention.
```

- Tech:

```markdown
Huggingface, Polygon+Ethereum, Filecoin/IPFS, Biconomy, Auth0, NextJs, MongoDB-Atlas, ExpressJS, etherjs, React-native.
```

- MongoDB:

```markdown
MongoDB stands as the cornerstone of CloakR's crime reporting platform, offering scalability, real-time data updates, flexible data modeling, geospatial capabilities, and robust security. As CloakR aims to revolutionize crime reporting, MongoDB's ability to seamlessly accommodate data influx from AI-powered "Listeners," law enforcement submissions, and user tips ensures a current and comprehensive crime database. MongoDB's flexible schema-less design adapts effortlessly to evolving data structures, supporting the diverse nature of crime-related information and rapid development. With geospatial features enhancing localized crime data delivery and stringent security measures, MongoDB's pivotal role solidifies CloakR's commitment to privacy, accuracy, and community safety.
```

- Replit:

```markdown
To make sure our platform works well, we needed a big and constantly updated database that can handle contributions from users all over the country, even if not all regions of the police are involved equally. To solve this issue, we came up with something called a "Listener." It's like a watchful helper that keeps checking online news sources all the time. Using advanced techniques to read websites and a really smart computer program, this Listener collects important information about crimes from those sources. This clever idea helps us keep our database strong and always filled with the latest data. This way, people from different parts of the country can join in, help stop crimes, and even get rewards. We deployed this entire system program work on Replit so that it can monitor outlet 24/7. Replit's seamless integration of code development, deployment, and management simplifies the complex processes involved in maintaining a dynamic crime reporting ecosystem. By harnessing Replit's capabilities, we create a user-centric, reliable, and powerful platform that empowers individuals across the country to actively contribute to community safety, thereby making our choice of Replit a strategic and exceptional one.
```

- Auth0

```
The implementation of Auth0 within CloakR offers a robust and user-centric solution for Aadhar verification. Auth0's sophisticated authentication and identity management capabilities ensure a seamless and secure process, enhancing user trust and confidence. By enabling Aadhar verification through OTP with registered mobile numbers, Auth0 not only reinforces data security but also streamlines the user experience, aligning perfectly with CloakR's commitment to anonymity, privacy, and efficient crime reporting.
```

- GitHub

```
Our implementation showcases a unique and innovative utilization of GitHub, reflecting our strategic and well-orchestrated approach to project management and collaboration. Through the establishment of a dedicated organization and the adoption of a microservices architecture, we have not only embraced the principles of modularity and scalability but have also created an environment where efficient coordination and development thrive. By partitioning the project into distinct repositories within the same organization, we've harnessed the power of focused development, enabling us to dedicate resources to specific components while ensuring seamless integration and interoperability. This approach has empowered our team members to work in parallel, enhancing productivity and ensuring a streamlined development process. Our utilization of GitHub's collaborative features, coupled with the meticulous organization of repositories, underscores our commitment to innovation, effective teamwork, and the realization of a comprehensive and impactful solution that has the potential to reshape crime reporting and community safety.
```

- Postman

```
Employing Postman for API testing has been a pivotal step in ensuring the seamless integration between our frontend and database components. By rigorously testing our APIs, we've been able to establish a robust and reliable communication channel that facilitates the efficient exchange of data. Postman's user-friendly interface and comprehensive testing capabilities have enabled us to validate the functionality of our APIs, detect potential issues, and fine-tune the interactions between different parts of our platform. This meticulous testing process not only enhances the user experience but also bolsters the overall integrity and performance of our solution, showcasing our dedication to delivering a seamless and user-centric crime reporting platform.
```
