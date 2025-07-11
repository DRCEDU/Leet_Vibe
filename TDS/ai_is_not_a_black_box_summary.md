# AI Is Not a Black Box (Relatively Speaking)

*Source: [Towards Data Science](https://towardsdatascience.com/ai-is-not-a-black-box/), by Piotr (Peter) Mardziel, Jun 13, 2025*

## Summary

This article argues that artificial intelligence (AI) is, in many ways, more transparent than human intelligence. While AI is often called a "black box," the author contends that compared to the opacity of the human mind, AI systems are relatively open to inspection and analysis.

## Key Points

- **Transparency of AI vs. Humans:**
  - Human minds are mysterious and difficult to interrogate or understand, even with advanced tools like fMRI.
  - AI systems, especially open-source models, can be probed, inspected, and analyzed at a much deeper level than is possible with human brains.

- **Types of Black Box Access:**
  - *Black box access* refers to not being able to inspect the code or parameters of proprietary models (e.g., ChatGPT).
  - *White box access* means full access to the model's internals, but even then, understanding the model's operation can be challenging.

- **Comparative Opacity:**
  - The human brain is more of a black box than even closed-source AI models, due to physical and ethical constraints on experimentation.
  - AI models can be analyzed in ways that are impossible for human brains, such as tracing the path of a concept through a neural network.

- **Interpretability and Analysis:**
  - In AI, we can:
    - Associate neural activity with specific concepts (akin to fMRI in humans).
    - Determine the importance of specific inputs to outputs.
    - Trace the path of concepts through the network (e.g., subject-number agreement in BERT).
  - For humans, self-reporting is unreliable due to bias, lack of self-awareness, or dishonesty.
  - AI interpretability does not rely on the AI's self-reporting; we can directly inspect its "neurons."

- **Open Source vs. Closed Source:**
  - Open source models allow for full inspection and analysis.
  - Even with closed-source models, much can be inferred through controlled experiments and model distillation.

- **Stability and Future Outlook:**
  - The architectures of top-performing models have remained stable, and transparency is likely to persist even as AI capabilities grow.
  - There is no indication that human brain research will surpass the transparency available in AI systems.

## Notable Figures/Diagrams (Described)

- **Fig 1 & 3:** Visualizations of 425,000 concepts in Google's Gemma2-2B model, color-coded by layer.
- **Fig 2:** fMRI-captured volume of the human brain, illustrating the limitations of current brain mapping.
- **Fig 4:** Path tracing of subject-number agreement through the layers of a BERT model.

## Selected Quotes

> "Artificial intelligence—while still mysterious—is crystal clear in comparison. I can probe an AI for its equivalent of thoughts and motivations and know I’m getting the truth."

> "The human mind is more of a black box—albeit an organic, carbon-based, 'natural' one—than even the proprietary, closed-source AI models."

> "We can tell whether an AI is 'thinking' about a particular concept. How well can we tell when a human is thinking about a particular concept?"

> "Methods for interpretability in the AI space do not rely on AI’s answers, truthful, unbiased, self-aware, or otherwise. We don’t need to trust the AI’s outputs in order to tell whether it is thinking about a particular concept."

## Conclusion

The article concludes that AI is not the black box it is often made out to be. In fact, compared to the human mind, AI systems are relatively transparent and open to analysis, especially when open source. The author suggests that this transparency can be a foundation for understanding and trust in AI systems. 