---

layout: post
date: 2022-07-23
title: Rules of the Software Development Game

---


1. If there is a question, a problem, a concern, an issue then create an issue in whatever backlog/workflow tool you are using.
    - Search first for open issues to make sure it's not a duplicate, if you do find another, then update it and add context.
    - Use a common framework for the content, e.g., acceptance criteria in a `given, when, then` format.
    - Do not create issues with nothing more than a title, it can cause panic/alarm if it is a security issue. Context is important so make sure it is provided.

2. Always provide context - Context switching costs are non-trivial. Courteous collaborators provide teammates with the necessary context to get up to speed on a discussion, and decide what, if any action they need to take. Pull requests titled “a few edits” or “minor improvements” do the exact opposite.

3. Issues exist to be an organisational to-do. They are there to be organised, discussed, challenged, assigned and to be done!

4. Show work early. Code speaks louder than words. Make a draft PR from the get go.

5. link it. Simply put, if you reference something - be it prior issue, the pull request that implemented a feature, a line in a file, whatever — and that thing has a URL, it’s your obligation to find that URL and make that reference a link

6. Speak and Engage with teams, it's better to ask a team for a support or action than individuals. Individual communication is often hidden from others and as such if that individual contributor gets hit by the proverbial bus or takes unexpected sick leave then message can get lost. Use team channels and the chances are you'll get a resolution sooner as more eyes will be on the request and it's more likely to end up as a task for a skilled contributor who can action the request as quickly as possible.

7. Build, from day one, for your eventual departure. At no point should any piece of work be tied to an individual. Do not become a bottleneck, a single point of responsibility as that will almost certainly lead to failure. Document, delegate, and train others.

8. Keep work as small as possible but no smaller. The smaller the work item, the small the change, the easier it is to test, to PR and to push through the pipeline to production. Don't try and force work to be uncomfortably smaller than is possible, this will just create blockers, dependencies, and frustration in not being able to test effectively.

9. Test everything.

10. Do not reinvent the wheel. Many aspects of software development are solved problems. Depending on organisational risk profiles it will often be more effective to use an existing package, solution, pattern than creating your own. But do consider longevity, quality, security, risk etc.