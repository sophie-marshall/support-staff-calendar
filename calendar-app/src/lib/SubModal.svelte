<script lang="ts">
	import SubForm from './SubForm.svelte';

	let availableStaff: string[] = ['Sophie', 'Crystal'];
</script>

<div class="sub-modal">
	<h3>Let's get the details ...</h3>
	<div class="modal-and-results">
		<SubForm />
		<div class="results">
			Search Results
			{#each availableStaff as subOption}
				<div class="sub-option">
					{subOption}
				</div>
			{/each}
		</div>
	</div>
</div>

<style>
	.sub-modal {
		display: flex;
		flex-direction: column;
		gap: 20px;
		width: 100%;
		background: black;
		color: white;
		padding: 20px;
	}

	.modal-and-results {
		display: grid;
		grid-template-columns: 1fr 1fr;
		gap: 20px;
	}

	.results {
		display: flex;
		flex-direction: column;
		align-content: flex-start;
		gap: 5px;
	}

	.sub-option {
		background: white;
		color: blue;
		padding: 5px 10px;
	}
</style>
