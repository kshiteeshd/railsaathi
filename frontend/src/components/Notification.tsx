import { useEffect } from "react";
import type { NotificationType } from "../types/notification";
import "./Notification.css";

interface NotificationProps {
  type: NotificationType;
  title: string;
  message: string;
  duration?: number;
  onClose: () => void;
}

const icons: Record<NotificationType, string> = {
  success: "✓",
  error: "!",
  warning: "!",
  info: "i",
};

function Notification({
  type,
  title,
  message,
  duration = 4000,
  onClose,
}: NotificationProps) {
  useEffect(() => {
    const timer = window.setTimeout(onClose, duration);

    return () => window.clearTimeout(timer);
  }, [duration, onClose]);

  return (
    <div className={`notification notification-${type}`}>
      <div className="notification-glass">
        <div className="notification-light" />

        <div className="notification-icon">{icons[type]}</div>

        <div className="notification-content">
          <h4>{title}</h4>
          <p>{message}</p>
        </div>

        <button
          type="button"
          className="notification-close"
          onClick={onClose}
          aria-label="Close notification"
        >
          ×
        </button>

        <div
          className="notification-progress"
          style={{ animationDuration: `${duration}ms` }}
        />
      </div>
    </div>
  );
}

export default Notification;
