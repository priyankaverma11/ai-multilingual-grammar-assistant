type SubmitButtonProps = {
  onClick: () => void;
  loading: boolean;
};

export default function SubmitButton({
  onClick, loading,
}: SubmitButtonProps) {
  return (
    <button
      onClick={onClick}
      disabled={loading}
      className="bg-black text-white px-6 py-3 rounded-lg mt-4"
    >
      {loading ? "Correcting..." : "Correct Grammar"}
    </button>
  );
}