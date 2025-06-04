### Comparison

| Feature      | VM                                   | App Service                          |
|--------------|--------------------------------------|--------------------------------------|
| Cost         | Higher (pay for uptime even if idle) | Lower (pay per use)                  |
| Scalability  | Manual scaling required              | Auto-scaling supported               |
| Availability | Requires setup (load balancer, etc.) | Built-in high availability           |
| Workflow     | Full control, more complex setup     | Simple CI/CD, low maintenance        |

---

### My Choice: App Service

I chose **App Service** because it offers seamless scaling, simplified deployment (including GitHub integration), and built-in availability. It’s ideal for hosting lightweight web applications like a CMS. The App Service plan helps reduce maintenance overhead and supports fast development cycles, which aligns well with this project’s requirements.

The CMS app mostly handles CRUD operations, form submissions, and image uploads—features that don't require custom OS control or high compute resources. App Service is better suited for such workloads and keeps costs lower.

---

### When I Would Choose a VM Instead

If the application evolved to include:

- **Background services** or scheduled tasks
- **High-performance processing** (e.g., video rendering, ML inference)
- **Custom OS-level dependencies or security requirements**
- **VPN integration or advanced networking rules**

Then a **VM** would be the better choice. A VM provides full access to the OS, so you can install any libraries or configurations required, and tailor the infrastructure to the app’s needs.

---

### App Change Assessment

If my app required any of the above features—like persistent background jobs or access to GPU/CPU-intensive compute—I would switch to a VM. That setup would allow for complete control over the environment, despite being harder to maintain and more expensive.

In contrast, since the current CMS application is simple, lightweight, and stateless, App Service is the best choice.

---

### Logging Evidence

Logging was implemented using `app.logger.info()` within the `views.py` login route. This captures both:

- Failed logins: `Invalid login attempt for username: user123`
- Successful logins: `User admin logged in successfully`

These log messages appear in the terminal console when running the app locally.

> **Note**: My Azure sandbox environment expired, so live Azure logs are unavailable. However, the local environment uses the same logic that was previously deployed, ensuring the same logging behavior.

---

