document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("registerForm");
    if (!form) return;

    form.addEventListener("submit", handleSubmit);

    async function handleSubmit(e) {
        e.preventDefault();
        
        const getValue = id => document.getElementById(id)?.value.trim();
        
        const user = {
            name: getValue("name"),
            email: getValue("email"),
            password: getValue("password")
        };

        if (!user.name || !user.email || !user.password) {
            alert("Please fill all fields");
            return;
        }

        try {
            const response = await fetch("http://localhost:8080/api/v1/register", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify(user)
            });

            const data = await response.json();
            
            if (!response.ok) throw new Error(data.message || "Registration failed");
            
            alert("Success! Redirecting...");
            setTimeout(() => window.location.href = "login.html", 500);
            
        } catch (error) {
            console.error("Error:", error);
            alert(error.message);
        }
    }
});