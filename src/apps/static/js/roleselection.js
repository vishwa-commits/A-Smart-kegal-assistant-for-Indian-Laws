document.addEventListener("DOMContentLoaded", function () {
    const rolePages = {
        'Judge': 'judgedashboard.html', // Changed from login.html to direct page
        'Advocate/Lawyer': 'advocatedashboard.html',
        'Woman': 'woman.html',
        'Citizen': 'citizen.html',
        'Student': 'studentdashboard.html',
        'Minor': 'minor.html'
    };

    function selectRole(role) {
        if (!role || !rolePages[role]) {
            console.error("❌ Invalid role selected:", role);
            return;
        }
        
        console.log("✅ Role selected:", role);
        window.location.href = rolePages[role];
    }

    document.querySelectorAll(".role").forEach(button => {
        button.addEventListener("click", function () {
            const role = this.getAttribute("data-role");
            selectRole(role);
        });
    });

    // Modified logout button (simple navigation)
    document.getElementById("logoutBtn")?.addEventListener("click", function (e) {
        e.preventDefault();
        window.location.href = "/roleselection.html"; // Direct navigation back
    });
});