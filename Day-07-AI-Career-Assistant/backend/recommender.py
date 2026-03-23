try:
    from sentence_transformers import SentenceTransformer, util
except ImportError:
    SentenceTransformer = None
    print("SentenceTransformer not installed, using mock")

class RecommenderSystem:
    def __init__(self):
        if SentenceTransformer:
            # Load model (this involves downloading, so might take time on first run)
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
        else:
            self.model = None

    def get_embedding(self, text):
        if self.model:
            return self.model.encode(text)
        return [0.0] * 384 # Mock embedding

    def find_best_matches(self, user_embedding, jobs_data, top_k=5):
        """
        jobs_data: List of dicts/tuples with (id, title, skills, embedding_list)
        Returns: List of (job, score) sorted by score.
        """
        if not jobs_data:
            return []
            
        if not self.model:
            # Fallback: Return top k jobs with 0.0 score so the UI isn't empty
            print("Model not loaded, returning fallback results")
            return [(job, 0.0) for job in jobs_data[:top_k]]
        
        import torch
        
        # Convert user embedding to tensor
        query_emb = torch.tensor(user_embedding)
        
        # Prepare job embeddings
        # Assuming jobs_data has 'embedding' key/attr which is a list or tensor
        # We need to stack them
        job_embeddings = [job['embedding'] for job in jobs_data]
        corpus_emb = torch.tensor(job_embeddings)
        
        # Compute cosine similarity
        # util.cos_sim returns a matrix
        scores = util.cos_sim(query_emb, corpus_emb)[0]
        
        # Combine with job data
        results = []
        for idx, score in enumerate(scores):
            results.append((jobs_data[idx], score.item()))
        
        # Sort by score descending
        results.sort(key=lambda x: x[1], reverse=True)
        
        return results[:top_k]
