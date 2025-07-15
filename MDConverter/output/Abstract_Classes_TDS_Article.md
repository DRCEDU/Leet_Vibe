---
title: "Abstract Classes: A Software Engineering Concept Data Scientists Must Know To Succeed | Towards Data Science"
og_title: "Abstract Classes: A Software Engineering Concept Data Scientists Must Know To Succeed | Towards Data Science"
description: "Simple concepts that differentiate a professional from amateurs."
url: "https://towardsdatascience.com/abstract-classes-a-software-engineering-concept-data-scientists-must-know-to-succeed/"
published: "2025-06-17T22:45:07+00:00"
author: "Benjamin Lee"
---

# Abstract Classes: A Software Engineering Concept Data Scientists Must Know To Succeed | Towards Data Science

## Article Information

**Author:** Benjamin Lee
**Published:** 2025-06-17T22:45:07+00:00
**Original URL:** https://towardsdatascience.com/abstract-classes-a-software-engineering-concept-data-scientists-must-know-to-succeed/

**Description:** Simple concepts that differentiate a professional from amateurs.

---

[Data Science](https://towardsdatascience.com/category/data-science/)


# Abstract Classes: A Software Engineering Concept Data Scientists Must Know To Succeed

Simple concepts that differentiate a professional from amateurs.

[Benjamin Lee](https://towardsdatascience.com/author/bl3e967/)

Jun 17, 2025

13 min read

Share

![Image](images/chris-ried-ieic5Tq8YMk-unsplash-scaled-1.jpg)

[Image](https://unsplash.com/fr/photos/un-ecran-dordinateur-avec-un-tas-de-code-dessus-ieic5Tq8YMk) by Chris Ried via Unsplash


## Why you should read this article

If you are planning to go into data science, be it a graduate or a professional looking for a career change, or a manager in charge of establishing best practices, this article is for you.

Data science attracts a variety of different backgrounds. From my professional experience, I’ve worked with colleagues who were once:


- Nuclear physicists

- Post-docs researching gravitational waves

- PhDs in computational biology

- Linguists

just to name a few.

It is wonderful to be able to meet such a diverse set of backgrounds and I have seen such a variety of minds lead to the growth of a creative and effective data science function.

However, I have also seen one big downside to this variety:


> *Everyone has had different levels of exposure to key Software Engineering concepts, resulting in a patchwork of coding skills.*

As a result, I have seen work done by some data scientists that is brilliant, but is:


- Unreadable — you have no idea what they are trying to do.

- Flaky — it breaks the moment someone else tries to run it.

- Unmaintainable — code quickly becomes obsolete or breaks easily.

- Un-extensible — code is single-use and its behaviour cannot be extended

which ultimately dampens the impact their work can have and creates all sorts of issues down the line.

So, in a series of articles, I plan to outline some core software engineering concepts that I have tailored to be necessities for data scientists.

They are simple concepts, but the difference between knowing them vs not knowing them clearly draws the line between amateur and professional.

![Image](images/steve-johnson-VCLNNMRl07k-unsplash-1024x683.jpg)

Abstract Art, Photo by [Steve Johnson](https://unsplash.com/@steve_j?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/orange-red-and-blue-abstract-painting-VCLNNMRl07k?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)


## Today’s concept: Abstract classes

Abstract classes are an extension of class inheritance, and it can be a very useful tool for data scientists if used correctly.


> *If you need a refresher on class inheritance, see my article on it [here](https://towardsdatascience.com/inheritance-a-software-engineering-concept-data-scientists-must-know-to-succeed/)*.

Like we did for [class inheritance](https://towardsdatascience.com/inheritance-a-software-engineering-concept-data-scientists-must-know-to-succeed/), I won’t bother with a formal definition. Looking back to when I first started coding, I found it hard to decipher the vague and abstract (no pun intended) definitions out there in the Internet.

It’s much easier to illustrate it by going through a practical example.

So, let’s go straight into an example that a data scientist is likely to encounter to demonstrate how they are used, and why they are useful.


## Example: Preparing data for ingestion into a feature generation pipeline

![Image](images/scott-graham-5fNmWej4tAA-unsplash-1024x683.jpg)

Photo by [Scott Graham](https://unsplash.com/@amstram?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on [Unsplash](https://unsplash.com/photos/person-holding-pencil-near-laptop-computer-5fNmWej4tAA?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash)

Let’s say we are a consultancy that specialises in fraud detection for financial institutions.

We work with a number of different clients, and we have a set of features that carry a consistent signal across different client projects because they embed domain knowledge gathered from subject matter experts.

So it makes sense to build these features for each project, even if they are dropped during feature selection or are replaced with bespoke features built for that client.


### The challenge

We data scientists know that working across different projects/environments/clients means that the input data for each one is never the same;


- Clients may provide different file types: `CSV`, `Parquet`, `JSON`, `tar`, to name a few.

- Different environments may require different sets of credentials.

- Most definitely each dataset has their own quirks and so each one requires different data cleaning steps.

Therefore, you may think that we would need to build a new feature generation pipeline for each and every client.

How else would you handle the intricacies of each dataset?


### No, there is a better way

Given that:


- We know we’re going to be building the *same* set of useful features for each client

- We can build one feature generation pipeline that can be reused for each client

- Thus, the only new problem we need to solve is cleaning the input data.

Thus, our problem can be formulated into the following stages:

![Image](images/image-10-1024x210.png)

Image by author. Blue circles are datasets, yellow squares are pipelines.


- Data Cleaning pipeline
 - Responsible for handling any unique cleaning and processing that is required for a given client in order to format the dataset into a *standardised schema* dictated by the feature generation pipeline.

- The Feature Generation pipeline
 - Implements the feature engineering logic assuming the input data will follow a fixed schema to output our useful set of features.

Given a fixed input data schema, building the feature generation pipeline is trivial.

Therefore, we have boiled down our problem to the following:


> *How do we ensure the quality of the data cleaning pipelines such that their outputs always adhere to the downstream requirements?*


## The *real* problem we are solving

Our problem of *‘ensuring the output always adhere to downstream requirements’* is not just about getting code to run. That’s the easy part.

The hard part is designing code that is robust to a myriad of external, non-technical factors such as:


- Human error
 - People naturally forget small details or prior assumptions. They may build a data cleaning pipeline whilst overlooking certain requirements.

- Leavers
 - Over time, your team inevitably changes. Your colleagues may have knowledge that they assumed to be obvious, and therefore they never bothered to document it. Once they have left, that knowledge is lost. Only through trial and error, and hours of debugging will your team ever recover that knowledge.

- New joiners
 - Meanwhile, new joiners have no knowledge about prior assumptions that were once assumed obvious, so their code usually requires a lot of debugging and rewriting.

This is where abstract classes really shine.


## Input data requirements

We mentioned that we can fix the schema for the feature generation pipeline input data, so let’s define this for our example.

Let’s say that our pipeline expects to read in *parquet* files, containing the following columns:

```
```yaml
row_id:
 int, a unique ID for every transaction.
timestamp:
 str, in ISO 8601 format. The timestamp a transaction was made.
amount: 
 int, the transaction amount denominated in pennies (for our US readers, the equivalent will be cents).
direction: 
 str, the direction of the transaction, one of ['OUTBOUND', 'INBOUND']
account_holder_id: 
 str, unique identifier for the entity that owns the account the transaction was made on.
account_id: 
 str, unique identifier for the account the transaction was made on.
```
```

Let’s also add in a requirement that the dataset must be ordered by `timestamp`.


## The abstract class

Now, time to define our abstract class.

An abstract class is essentially a blueprint from which we can inherit from to create child classes, otherwise named ‘*concrete*‘ classes.

Let’s spec out the different methods we may need for our data cleaning blueprint.

```
```python
import os
from abc import ABC, abstractmethod

class BaseRawDataPipeline(ABC):
 def __init__(
 self,
 input_data_path: str | os.PathLike,
 output_data_path: str | os.PathLike
 ):
 self.input_data_path = input_data_path
 self.output_data_path = output_data_path

 @abstractmethod
 def transform(self, raw_data):
 """Transform the raw data.
 
 Args:
 raw_data: The raw data to be transformed.
 """
 ...

 @abstractmethod
 def load(self):
 """Load in the raw data."""
 ...

 def save(self, transformed_data):
 """save the transformed data."""
 ...

 def validate(self, transformed_data):
 """validate the transformed data."""
 ...

 def run(self):
 """Run the data cleaning pipeline."""
 ...
```
```

You can see that we have imported the `ABC` class from the `abc` module, which allows us to create abstract classes in Python.

![Image](images/image-63-1024x572.png)

Image by author. Diagram of the abstract class and concrete class relationships and methods.


## Pre-defined behaviour

![Image](images/image-64-1024x572.png)

Image by author. The methods to be pre-defined are circled red.

Let’s now add some pre-defined behaviour to our abstract class.

Remember, this behaviour will be made available to all child classes which inherit from this class so this is where we bake in behaviour that you want to enforce for all future projects.

For our example, the behaviour that needs fixing across all projects are all related to how we output the processed dataset.


### 1. The `run` method

First, we define the `run` method. This is the method that will be called to run the data cleaning pipeline.

```
```python
 def run(self):
 """Run the data cleaning pipeline."""
 inputs = self.load()
 output = self.transform(*inputs)
 self.validate(output)
 self.save(output)
```
```

The run method acts as a single point of entry for all future child classes.

This standardises how any data cleaning pipeline will be run, which enables us to then build new functionality around any pipeline without worrying about the underlying implementation.

You can imagine how incorporating such pipelines into some orchestrator or scheduler will be easier if all pipelines are executed through the same `run` method, as opposed to having to handle many different names such as `run`, `execute`, `process`, `fit`, `transform` etc.


### 2. The `save` method

Next, we fix how we output the transformed data.

```
```python
 def save(self, transformed_data:pl.LazyFrame):
 """save the transformed data to parquet."""
 transformed_data.sink_parquet(
 self.output_file_path,
 )
```
```

We’re assuming we will use `polars` for data manipulation, and the output is saved as `parquet` files as per our specification for the feature generation pipeline.


### 3. The `validate` method

Finally, we populate the `validate` method which will check that the dataset adheres to our expected output format before saving it down.

```
```python
 @property
 def output_schema(self):
 return dict(
 row_id=pl.Int64,
 timestamp=pl.Datetime,
 amount=pl.Int64,
 direction=pl.Categorical,
 account_holder_id=pl.Categorical,
 account_id=pl.Categorical,
 )
 
 def validate(self, transformed_data):
 """validate the transformed data."""
 schema = transformed_data.collect_schema()
 assert (
 self.output_schema == schema, 
 f"Expected {self.output_schema} but got {schema}"
 )
```
```

We’ve created a property called `output_schema`. This ensures that all child classes will have this available, whilst preventing it from being accidentally removed or overridden if it was defined in, for example, `__init__`.


## Project-specific behaviour

![Image](images/image-65-1024x572.png)

Image by author. Project specific methods that need to be overridden are circled red.

In our example, the `load` and `transform` methods are where project-specific behaviour will be held, so we leave them blank in the base class – the implementation is deferred to the future data scientist in charge of writing this logic for the project.

You will also notice that we have used the `abstractmethod` decorator on the `transform` and `load` methods. This decorator enforces these methods to be defined by a child class. If a user forgets to define them, an error will be raised to remind them to do so.

Let’s now move on to some example projects where we can define the `transform` and `load` methods.


## Example project

The client in this project sends us their dataset as CSV files with the following structure:

```
```yaml
event_id: str
unix_timestamp: int
user_uuid: int
wallet_uuid: int
payment_value: float
country: str
```
```

We learn from them that:


- Each transaction is unique identified by the combination of `event_id` and `unix_timestamp`

- The `wallet_uuid` is the equivalent identifier for the ‘account’

- The `user_uuid` is the equivalent identifier for the ‘account holder’

- The `payment_value` is the transaction amount, denominated in Pound Sterling (or Dollar).

- The CSV file is separated by `|` and has no header.


### The concrete class

Now, we implement the `load` and `transform` functions to handle the unique complexities outlined above in a child class of `BaseRawDataPipeline`.

Remember, these methods are all that need to be written by the data scientists working on this project. All the aforementioned methods are pre-defined so they need not worry about it, reducing the amount of work your team needs to do.


#### 1. Loading the data

The `load` function is quite simple:

```
```python
class Project1RawDataPipeline(BaseRawDataPipeline):

 def load(self):
 """Load in the raw data.
 
 Note:
 As per the client's specification, the CSV file is separated 
 by `|` and has no header.
 """
 return pl.scan_csv(
 self.input_data_path,
 sep="|",
 has_header=False
 )
```
```

We use polars’ `scan_csv` [method](https://docs.pola.rs/api/python/dev/reference/api/polars.scan_csv.html) to stream the data, with the appropriate arguments to handle the CSV file structure for our client.


#### 2. Transforming the data

The transform method is also simple for this project, since we don’t have any complex joins or aggregations to perform. So we can fit it all into a single function.

```
```python
class Project1RawDataPipeline(BaseRawDataPipeline):

 ...

 def transform(self, raw_data: pl.LazyFrame):
 """Transform the raw data.

 Args:
 raw_data (pl.LazyFrame):
 The raw data to be transformed. Must contain the following columns:
 - 'event_id'
 - 'unix_timestamp'
 - 'user_uuid'
 - 'wallet_uuid'
 - 'payment_value'

 Returns:
 pl.DataFrame:
 The transformed data.

 Operations:
 1. row_id is constructed by concatenating event_id and unix_timestamp
 2. account_id and account_holder_id are renamed from user_uuid and wallet_uuid
 3. transaction_amount is converted from payment_value. Source data
 denomination is in £/$, so we need to convert to p/cents.
 """

 # select only the columns we need

 DESIRED_COLUMNS = [
 "event_id",
 "unix_timestamp",
 "user_uuid",
 "wallet_uuid",
 "payment_value",
 ]
 df = raw_data.select(DESIRED_COLUMNS)

 df = df.select(
 # concatenate event_id and unix_timestamp

 # to get a unique identifier for each row.

 pl.concat_str(
 [
 pl.col("event_id"),
 pl.col("unix_timestamp")
 ],
 separator="-"
 ).alias('row_id'),

 # convert unix timestamp to ISO format string

 pl.from_epoch("unix_timestamp", "s").dt.to_string("iso").alias("timestamp"),

 pl.col("user_uuid").alias("account_id"),
 pl.col("wallet_uuid").alias("account_holder_id"),

 # convert from £ to p

 # OR convert from $ to cents

 (pl.col("payment_value") * 100).alias("transaction_amount"),
 )

 return df
```
```

Thus, by overloading these two methods, we’ve implemented all we need for our client project.

The output we know conforms to the requirements of the downstream feature engineering pipeline, so we automatically have assurance that our outputs are compatible.


> ***No debugging required. No hassle. No fuss.***


## Final summary: Why use abstract classes in data science pipelines?

Abstract classes offer a powerful way to bring consistency, robustness, and improved maintainability to data science projects. By using Abstract Classes like in our example, our data science team sees the following benefits:


## 1. No need to worry about compatibility

By defining a clear blueprint with abstract classes, the data scientist only needs to focus on implementing the `load` and `transform` methods specific to their client’s data.

As long as these methods conform to the expected input/output types, compatibility with the downstream feature generation pipeline is guaranteed.

This separation of concerns simplifies the development process, reduces bugs, and accelerates development for new projects.


### 2. Easier to document

The structured format naturally encourages in-line documentation through method docstrings.

This proximity of design decisions and implementation makes it easier to communicate assumptions, transformations, and nuances for each client’s dataset.

Well-documented code is easier to read, maintain, and hand over, reducing the knowledge loss caused by team changes or turnover.


### 3. Improved code readability and maintainability

With abstract classes enforcing a consistent interface, the resulting codebase avoids the pitfalls of unreadable, flaky, or unmaintainable scripts.

Each child class adheres to a standardized method structure (`load`, `transform`, `validate`, `save`, `run`), making the pipelines more predictable and easier to debug.


### 4. Robustness to human factors

Abstract classes help reduce risks from human error, teammates leaving, or learning new joiners by embedding essential behaviours in the base class. This ensures that critical steps are never skipped, even if individual contributors are unaware of all downstream requirements.


### 5. Extensibility and reusability

By isolating client-specific logic in concrete classes while sharing common behaviors in the abstract base, it becomes straightforward to extend pipelines for new clients or projects. You can add new data cleaning steps or support new file formats without rewriting the entire pipeline.

In summary, abstract classes levels up your data science codebase from ad-hoc scripts to scalable, and maintainable production-grade code. Whether you’re a data scientist, a team lead, or a manager, adopting these software engineering principles will significantly boost the impact and longevity of your work.


## Related articles:

If you enjoyed this article, then have a look at some of my other related articles.


- **Inheritance: A software engineering concept data scientists must know to succeed ([here](https://towardsdatascience.com/inheritance-a-software-engineering-concept-data-scientists-must-know-to-succeed/))**

- **Encapsulation: A softwre engineering concept data scientists must know to succeed ([here](https://medium.com/data-science/encapsulation-a-software-engineering-concept-data-scientists-must-know-to-succeed-b3b1a0a42a41))**

- **The Data Science Tool You Need For Efficient ML-Ops ([here](https://medium.com/ai-advances/the-data-science-tool-you-need-for-efficient-mlops-408d826bd48d))**

- **DSLP: The data science project management framework that transformed my team ([here](https://medium.com/data-science/dslp-the-data-science-project-management-framework-that-transformed-my-team-1b6727d009aa))**

- **How to stand out in your data scientist interview ([here](https://medium.com/data-science/how-to-stand-out-in-your-data-scientist-interview-f3cbaddbbae4))**

- **An Interactive Visualisation For Your Graph Neural Network Explanations ([here](https://medium.com/data-science/an-interactive-visualisation-for-your-graph-neural-network-explanations-1ac79d8ddd0a))**

- **The New Best Python Package for Visualising Network Graphs ([here)](https://medium.com/data-science/the-new-best-python-package-for-visualising-network-graphs-e220d59e054e)**

---

Written By

Benjamin Lee

[See all from Benjamin Lee](https://towardsdatascience.com/author/bl3e967/)

[Coding](https://towardsdatascience.com/tag/coding/), [Coding Best Practices](https://towardsdatascience.com/tag/coding-best-practices/), [Data Science](https://towardsdatascience.com/tag/data-science/), [Programming](https://towardsdatascience.com/tag/programming/), [Python](https://towardsdatascience.com/tag/python/)

Share This Article


- [Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Ftowardsdatascience.com%2Fabstract-classes-a-software-engineering-concept-data-scientists-must-know-to-succeed%2F&title=Abstract%20Classes%3A%20A%20Software%20Engineering%20Concept%20Data%20Scientists%20Must%20Know%20To%20Succeed)

- [Share on LinkedIn](https://www.linkedin.com/shareArticle?mini=true&url=https%3A%2F%2Ftowardsdatascience.com%2Fabstract-classes-a-software-engineering-concept-data-scientists-must-know-to-succeed%2F&title=Abstract%20Classes%3A%20A%20Software%20Engineering%20Concept%20Data%20Scientists%20Must%20Know%20To%20Succeed)

- [Share on X](https://x.com/share?url=https%3A%2F%2Ftowardsdatascience.com%2Fabstract-classes-a-software-engineering-concept-data-scientists-must-know-to-succeed%2F&text=Abstract%20Classes%3A%20A%20Software%20Engineering%20Concept%20Data%20Scientists%20Must%20Know%20To%20Succeed)

Towards Data Science is a community publication. Submit your insights to reach our global audience and earn through the TDS Author Payment Program.

[Write for TDS](https://towardsdatascience.com/questions-96667b06af5/)