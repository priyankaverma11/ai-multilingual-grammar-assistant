type LanguageCardProps = {
  language: string;
};

export default function LanguageCard({ language }: LanguageCardProps) {
  return (
    <div className="border rounded-lg p-4 mt-4">
      <h2 className="font-bold">Detected Language</h2>

      <p>{language}</p>
    </div>
  );
}
