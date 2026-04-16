# What are the most common debugging techniques?

- **Binary search** - Comment out the half of the code that may possibly be responsible for bugs
- **Explaining logic to a developer**

## Which tools are most effective for React debugging?

- **React Developer Tools** - Views the state of any component in the hierarchy
- **Redux DevTools** - Rewind actions to observe the changes of state over time
- **Storybook** - Isolate code blocks into a sandbox for testing before moving into the main code block

## How do you debug issues in large React codebases?

- Use React Error Boundaries to identify JavaScript errors in the child component, therefore isolating the crash
- Using AI to analyze repositories to identify patterns, suggest appropriate bug fixes and generate automatic tests
- Using React Profiler. It identifies performance issues due to redundant rendering
