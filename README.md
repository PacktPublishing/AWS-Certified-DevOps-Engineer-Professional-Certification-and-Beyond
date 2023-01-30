


# AWS Certified DevOps Engineer - Professional Certification and Beyond

<a href="https://www.packtpub.com/product/aws-certified-devops-engineer-professional-certification-and-beyond/9781801074452"><img src="https://static.packt-cdn.com/products/9781801074452/cover/smaller" alt="Book Name" height="256px" align="right"></a>

This is the code repository for [AWS Certified DevOps Engineer - Professional Certification and Beyond](https://www.packtpub.com/product/aws-certified-devops-engineer-professional-certification-and-beyond/9781801074452), published by Packt.

**Pass the DOP-C01 exam and prepare for the real world using case studies and real-life examples**

## What is this book about?
The AWS Certified DevOps Engineer certification is one of the highest AWS credentials, vastly recognized in cloud computing or software development industries. This book is an extensive guide to helping you strengthen your DevOps skills as you work with your AWS workloads on a day-to-day basis.

This book covers the following exciting features: 
* Automate your pipelines, build phases, and deployments with AWS-native tooling
* Discover how to implement logging and monitoring using AWS-native tooling
* Gain a solid understanding of the services included in the AWS DevOps Professional exam
* Reinforce security practices on the AWS platform from an exam point of view
* Find out how to automatically enforce standards and policies in AWS environments
* Explore AWS best practices and anti-patterns

If you feel this book is for you, get your [copy](https://www.amazon.com/Certified-DevOps-Engineer-Professional-Certification-ebook/dp/B099266M2M) today!

<a href="https://www.packtpub.com/?utm_source=github&utm_medium=banner&utm_campaign=GitHubBanner"><img src="https://raw.githubusercontent.com/PacktPublishing/GitHub/master/GitHub.png" alt="https://www.packtpub.com/" border="5" /></a>

## Instructions and Navigations
All of the code is organized into folders. For example, Chapter12.

The code will look like the following:
```
aws ec2 run-instances \
--image-id $AMI \
--instance-type t2.micro \
--user-data file://agents.sh \
--iam-instance-profile 'Name=CW_SSM' \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Ubuntu},{Key=Inspector,Value=TRUE}]' \
--region us-east-2

```

**Following is what you need for this book:**
This book is for AWS developers and SysOps administrators looking to advance their careers by achieving the highly sought-after DevOps Professional certification. Basic knowledge of AWS as well as its core services (EC2, S3, and RDS) is needed. Familiarity with DevOps concepts such as source control, monitoring, and logging, not necessarily in the AWS context, will be helpful.

With the following software and hardware list you can run all code files present in the book (Chapter 1-24).

### Software and Hardware List

| Chapter  | Software required                                                                                  | OS required                        |
| -------- | ---------------------------------------------------------------------------------------------------| -----------------------------------|
| 1-24     | AWS Account, AWS CLI, Python 3.x, Git									                            | Windows, Mac OS X, and Linux (Any) |


We also provide a PDF file that has color images of the screenshots/diagrams used in this book. [Click here to download it](https://static.packt-cdn.com/downloads/9781801074452_ColorImages.pdf).

### Related products <Other books you may enjoy>
* Implementing Identity Management on AWS [[Packt]](https://www.packtpub.com/product/implementing-identity-management-on-aws/9781800562288) [[Amazon]](https://www.amazon.com/Implementing-Identity-Management-AWS-environments/dp/1800562284)

* AWS for Solutions Architects [[Packt]](https://www.packtpub.com/product/aws-for-solutions-architects/9781789539233) [[Amazon]](https://www.amazon.com/AWS-Solutions-Architects-infrastructure-implementing/dp/1789539234)

## Get to Know the Author
**Adam Book**
He has been programming since the age of six and has been constantly tapped by founders and CEOs as one of the pillars to start their online or cloud businesses. Adam has developed applications, and websites. He’s been involved in cloud computing and datacenter transformation professionally since 1996 focusing on bringing the benefits of cloud computing to his clients. He’s led technology teams in transformative changes such as the shift to programming in sprints, with Agile formats. Adam is a cloud evangelist with a track record of migrating thousands of applications to the cloud and guiding businesses in understanding cloud economics to create use cases and identify operating model gaps. He has been certified on AWS since 2014.
### Download a free PDF

 <i>If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost.<br>Simply click on the link to claim your free PDF.</i>
<p align="center"> <a href="https://packt.link/free-ebook/9781801074452">https://packt.link/free-ebook/9781801074452 </a> </p>