import { useState } from "react";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Notification from "./components/Notification";
import type { NotificationType } from "./types/notification";

interface NotificationState {
  type: NotificationType;
  title: string;
  message: string;
}

function App() {
  const [showLogin, setShowLogin] = useState(true);

  const [notification, setNotification] = useState<NotificationState | null>(
    null,
  );

  const showNotification = (
    type: NotificationType,
    title: string,
    message: string,
  ) => {
    setNotification({
      type,
      title,
      message,
    });
  };

  return (
    <>
      {notification && (
        <Notification
          type={notification.type}
          title={notification.title}
          message={notification.message}
          onClose={() => setNotification(null)}
        />
      )}

      {showLogin ? (
        <Login
          onRegister={() => setShowLogin(false)}
          showNotification={showNotification}
        />
      ) : (
        <Register
          onLogin={() => setShowLogin(true)}
          showNotification={showNotification}
        />
      )}
    </>
  );
}

export default App;
